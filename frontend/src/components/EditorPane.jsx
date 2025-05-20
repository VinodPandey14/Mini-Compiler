import React from "react";

function EditorPane({ codeRef }) {
  return (
    <div className="editor-pane">
      <label htmlFor="code">Code Editor</label>
      <textarea id="code" placeholder="Write your code here..." ref={codeRef} />
    </div>
  );
}

export default EditorPane;
