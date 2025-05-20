import React from "react";

function CompileButton({ grammarRef, codeRef, setOutput }) {
  const handleCompile = () => {
    const code = document.getElementById("code").value;
    const grammar = document.getElementById("grammar").value;

    const data = { code, grammar };

    console.log("Data:", data);

    fetch("http://127.0.0.1:5000/compile", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        if (result.error) {
          console.error("Error:", result.error);
          setOutput({ tokens: [], parsed: "", ir: `Error: ${result.error}` });
        } else {
          console.log("Compilation result:", result);
          setOutput(result);
        }
      })
      .catch((error) => {
        console.error("Error compiling code:", error);
        setOutput({
          tokens: [],
          parsed: "",
          ir: `Network error: ${error.message}`,
        });
      });
  };

  return (
    <button className="compile-button" onClick={handleCompile}>
      Compile
    </button>
  );
}

export default CompileButton;
