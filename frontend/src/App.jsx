import "./styles/App.css";
import React, { useRef, useState } from "react";
import Header from "./components/Header";
import GrammarInput from "./components/GrammarInput";
import EditorPane from "./components/EditorPane";
import OutputPanel from "./components/OutputPanel";
import CompileButton from "./components/CompileButton";
import DefaultInputSelector from "./components/DefaultInputSelector";

export default function App() {
  const grammarRef = useRef();
  const codeRef = useRef();
  const [output, setOutput] = useState({ tokens: [], parsed: null, ir: "" });

  return (
    <div className="container">
      <Header />

      <div className="top-controls">
        <DefaultInputSelector grammarRef={grammarRef} codeRef={codeRef} />
      </div>

      <div className="main-section">
        <div className="panel">
          <GrammarInput grammarRef={grammarRef} />
        </div>
        <div className="panel">
          <EditorPane
            codeRef={codeRef}
          />
        </div>
      </div>

      <div className="compile-container">
        <CompileButton
          grammarRef={grammarRef}
          codeRef={codeRef}
          setOutput={setOutput}
        />
      </div>

      <div className="output-panel">
        <OutputPanel output={output} />
      </div>
    </div>
  );
}
