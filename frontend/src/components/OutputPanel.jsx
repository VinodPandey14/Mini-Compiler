import React, { useState, useRef } from "react";
import Tree from "react-d3-tree";
import "../styles/OutputPanel.css";

function OutputPanel({ output }) {
  const [showTokens, setShowTokens] = useState(false);
  const tokenDisplayLimit = 10;
  const treeContainerRef = useRef(null);

  const transformTokens = (tokens) => {
    return (tokens || []).map((t) => {
      if (typeof t === "object" && t.type && t.value !== undefined) {
        return { type: t.type, value: t.value };
      }
      return { type: "INVALID", value: JSON.stringify(t) };
    });
  };

  const transformParseTree = (node) => {
    if (!node) return null;
    if (typeof node === "string") return { name: node };
    if (typeof node === "object" && node.name) {
      return {
        name: node.name,
        children: (node.children || []).map(transformParseTree),
      };
    }
    return { name: "Unknown" };
  };

  const tokens = transformTokens(output.tokens || []);
  const treeData = output.parsed ? [transformParseTree(output.parsed)] : [];
  const semanticErrors = output.semanticErrors || [];

  const handleDownload = () => {
    let content = "=== Compiler Output Report ===\n\n";

    content += ">> Intermediate Code (IR):\n";
    content += (output.ir || "No IR generated") + "\n\n";

    content += ">> Tokens:\n";
    if (tokens.length > 0) {
      tokens.forEach((t, i) => {
        content += `${i + 1}. Type: ${t.type}, Value: ${t.value}\n`;
      });
    } else {
      content += "No tokens generated.\n";
    }

    content += "\n>> Parse Tree:\n";
    const getTreeText = (node, depth = 0) => {
      if (!node) return "";
      let text = `${" ".repeat(depth * 2)}- ${node.name}\n`;
      (node.children || []).forEach((child) => {
        text += getTreeText(child, depth + 1);
      });
      return text;
    };
    content += output.parsed ? getTreeText(output.parsed) : "No parse tree.\n";

    content += "\n>> Semantic Errors:\n";
    if (semanticErrors.length > 0) {
      semanticErrors.forEach((err, i) => {
        content += `${i + 1}. ${err.message} (Line ${err.line})\n`;
      });
    } else {
      content += "No semantic errors.\n";
    }

    content += "\n>> Target Code (MIPS):\n";
    content += (output.targetCode || "No target code generated") + "\n";

    const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "compiler_output.txt";
    link.click();
  };
  
  function downloadTreeAsSVG(containerRef, filename = "parse_tree.svg") {
    if (!containerRef?.current) return;

    const svgElement = containerRef.current.querySelector("svg");
    if (!svgElement) {
      console.warn("SVG element not found.");
      return;
    }

    svgElement.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svgElement.setAttribute("width", svgElement.scrollWidth);
    svgElement.setAttribute("height", svgElement.scrollHeight);

    const serializer = new XMLSerializer();
    const source = serializer.serializeToString(svgElement);

    const svgBlob = new Blob([source], { type: "image/svg+xml;charset=utf-8" });
    const url = URL.createObjectURL(svgBlob);

    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  return (
    <div className="output-panel">
      <h2>Compiler Output</h2>

      {/* Tokens */}
      <div className="tokens-section">
        <h3 onClick={() => setShowTokens(!showTokens)}>
          Tokens {showTokens ? "🔼" : "🔽"}
        </h3>
        <div className="token-list">
          <table>
            <thead>
              <tr>
                <th>Type</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
              {(showTokens ? tokens : tokens.slice(0, tokenDisplayLimit)).map(
                (token, index) => (
                  <tr key={index}>
                    <td>{token.type}</td>
                    <td>{token.value}</td>
                  </tr>
                )
              )}
            </tbody>
          </table>
          {tokens.length > tokenDisplayLimit && !showTokens && (
            <p className="more-hint">
              ...and {tokens.length - tokenDisplayLimit} more
            </p>
          )}
        </div>
      </div>

      {/* Parse Tree */}
      <div className="parse-tree-section">
        <h3>Parse Tree</h3>
        {treeData.length > 0 ? (
          <div className="tree-container" ref={treeContainerRef}>
            <Tree
              data={treeData}
              orientation="vertical"
              translate={{ x: 400, y: 100 }}
              separation={{ siblings: 1.5, nonSiblings: 2 }}
              collapsible={false}
            />
          </div>
        ) : (
          <p>No parse tree</p>
        )}
      </div>

      {/* Semantic Errors */}
      <div className="semantic-error-section">
        <h3>Semantic Errors</h3>
        {semanticErrors.length > 0 ? (
          <ul className="error-list">
            {semanticErrors.map((err, index) => (
              <li key={index} className="error-item">
                {index + 1}. {err.message} (Line {err.line})
              </li>
            ))}
          </ul>
        ) : (
          <p>No semantic errors found 🎉</p>
        )}
      </div>

      {/* IR */}
      <div className="ir-section">
        <h3>Intermediate Code (IR)</h3>
        <pre className="ir-box">{output.ir || "No IR generated"}</pre>
      </div>

      {/* Target Code (MIPS) */}
      <div className="target-section">
        <h3>Target Code (MIPS)</h3>
        <pre className="ir-box">
          {output.targetCode || "No target code generated"}
        </pre>
      </div>

        {/* Download Buttons */}
      <div className="download-section">
        <button onClick={handleDownload} className="download-btn">
          📄 Download Output
        </button>

        <button
          onClick={() => downloadTreeAsSVG(treeContainerRef)}
          className="download-btn"
        >
          🌳 Download Parse Tree
        </button>
      </div>
    </div>
  );
}

export default OutputPanel;
