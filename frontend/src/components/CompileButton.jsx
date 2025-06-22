import React from "react";

function CompileButton({ grammarRef, codeRef, setOutput }) {
  const handleCompile = () => {
    if (!grammarRef.current || !codeRef.current) {
      console.warn("Missing refs for grammar or code");
      setOutput({
        tokens: [],
        parsed: "",
        ir: "Error: Missing grammar or code input area",
      });
      return;
    }

    const grammar = grammarRef.current.getValue?.() || "";
    const code = codeRef.current.getValue?.() || "";

    const data = { grammar, code };

    console.log("Data:", data);

    fetch("https://mini-compiler-t39w.onrender.com/compile", {
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
          setOutput({
            tokens: [],
            parsed: "",
            ir: `Error: ${result.error}`,
          });
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
