import React from "react";

function OutputPanel({ output }) {
  const { tokens, parsed, ir } = output;

  return (
    <div className="output-panel">
      <h3>Tokens</h3>
      <pre>{tokens.length ? JSON.stringify(tokens, null, 2) : "No tokens"}</pre>

      <h3>Parse Result</h3>
      <pre>{parsed || "No parse result"}</pre>

      <h3>Intermediate Code</h3>
      <pre>{ir || "No intermediate representation"}</pre>
    </div>
  );
}

export default OutputPanel;
