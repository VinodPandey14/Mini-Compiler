import React, { useRef } from "react";
import Editor from "@monaco-editor/react";

function GrammarInput({ grammarRef }) {
  const editorInstance = useRef(null);

  const handleEditorMount = (editor) => {
    editorInstance.current = editor;
    grammarRef.current = editor; 
  };

  return (
    <div className="panel">
      <label>Grammar Rules</label>
      <Editor
        height="300px"
        defaultLanguage="plaintext"
        defaultValue=""
        onMount={handleEditorMount}
        theme="vs-light"
        options={{
          fontSize: 14,
          minimap: { enabled: false },
          wordWrap: "on",
        }}
      />
    </div>
  );
}

export default GrammarInput;
