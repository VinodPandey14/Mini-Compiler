import React from "react";

function GrammarInput({ grammarRef }) {
  return (
    <div className="grammar-input">
      <label htmlFor="grammar">Grammar Rules</label>
      <textarea
        id="grammar"
        placeholder="Enter grammar rules here..."
        ref={grammarRef}
      />
    </div>
  );
}

export default GrammarInput;
