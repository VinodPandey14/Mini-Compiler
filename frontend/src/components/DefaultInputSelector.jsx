import React from "react";
import { defaultExamples } from "../defaultInputs";

function DefaultInputSelector({ grammarRef, codeRef }) {
  
  const handleChange = (e) => {
    const selected = defaultExamples.find((d) => d.label === e.target.value);
    if (selected) {

      const grammar = (selected.grammar);
      const code = (selected.code);

      if (grammarRef.current?.setValue) {
        grammarRef.current.setValue(grammar);
      }

      if (codeRef.current?.setValue) {
        codeRef.current.setValue(code);
      }
    }
  };

  return (
    <div className="panel">
      <label htmlFor="defaultInput">Load Example</label>
      <select id="defaultInput" onChange={handleChange} defaultValue="">
        <option value="" disabled>
          Select a test case...
        </option>
        {defaultExamples.map((ex, index) => (
          <option key={index} value={ex.label}>
            {ex.label}
          </option>
        ))}
      </select>
    </div>
  );
}

export default DefaultInputSelector;
