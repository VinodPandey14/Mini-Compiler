import React, { useRef, useState } from "react";
import Header from "./components/Header";
import GrammarInput from "./components/GrammarInput";
import EditorPane from "./components/EditorPane";
import OutputPanel from "./components/OutputPanel";
import CompileButton from "./components/CompileButton";

function App() {
  const grammarRef = useRef();
  const codeRef = useRef();
  const [output, setOutput] = useState({ tokens: [], parsed: "", ir: "" });

  return (
    <div className="container">
      <Header />
      <div className="main-section">
        <GrammarInput grammarRef={grammarRef} />
        <EditorPane codeRef={codeRef} />
        <CompileButton
          grammarRef={grammarRef}
          codeRef={codeRef}
          setOutput={setOutput}
        />
        <OutputPanel output={output} />
      </div>
    </div>
  );
}

export default App;
