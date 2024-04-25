import React from 'react';
import { useState } from 'react';

function ScenarioForm({ onGenerate }) {
  const [prompt, setPrompt] = useState('');
  return (
    <div className="scenario-form">
      <form onSubmit={(e) => {
          e.preventDefault();
          onGenerate(prompt);
      }}>
          <textarea
            placeholder="Enter your scenario..."
            value={prompt}
            onChange={e => setPrompt(e.target.value)}
            rows="12"  // Increased from 3 to 5 for a bigger text area
            cols="50"
            style={{ resize: "none" }}  // Prevents resizing
        />
          <button type="submit" style={{ fontWeight: 'bold' }}>Generate Comic</button>
      </form>
    </div>
  );
}

export default ScenarioForm;





// import React, { useState } from 'react';

// function ScenarioForm({ onSubmitScenario }) {
//     const [scenario, setScenario] = useState('');

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         const response = await fetch('http://localhost:3001/generate', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ scenario })
//         });
//         const data = await response.json();
//         if (response.ok) {
//             onSubmitScenario(data.panels);
//         } else {
//             console.error('Failed to generate comics:', data);
//         }
//     };

//     return (
//         <form onSubmit={handleSubmit}>
//             <textarea
//                 value={scenario}
//                 onChange={(e) => setScenario(e.target.value)}
//                 placeholder="Enter your scenario..."
//                 rows="4"
//                 cols="50"
//             />
//             <button type="submit">Generate Comic</button>
//         </form>
//     );
// }

// export default ScenarioForm;


// import React, { useState } from 'react';

// function ScenarioForm({ onSubmitScenario }) {
//   const [scenario, setScenario] = useState('');

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     onSubmitScenario(scenario);
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <textarea
//         value={scenario}
//         onChange={(e) => setScenario(e.target.value)}
//         placeholder="Enter your scenario..."
//         rows="4"
//         cols="50"
//       />
//       <button type="submit">Generate Comic</button>
//     </form>
//   );
// }

// export default ScenarioForm;
