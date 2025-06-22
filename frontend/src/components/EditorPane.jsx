import React, { useRef } from "react";
import Editor from "@monaco-editor/react";

function EditorPane({ codeRef }) {
  const handleEditorMount = (editor) => {
    codeRef.current = {
      setValue: (value) => editor.setValue(value),
      getValue: () => editor.getValue(),
    };
  };

  return (
    <div className="panel">
      <h3>Code Editor</h3>
      <Editor
        height="300px"
        defaultLanguage="c"
        onMount={handleEditorMount}
        theme="vs-light"
        options={{
          fontSize: 14,
          wordWrap: "on",
          minimap: { enabled: false },
          lineNumbers: "off",
        }}
      />
    </div>
  );
}

export default EditorPane;
