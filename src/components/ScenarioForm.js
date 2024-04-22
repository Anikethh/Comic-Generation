import React from 'react';

function ScenarioForm({ onGenerate }) {
    return (
        <form onSubmit={(e) => {
            e.preventDefault();
            onGenerate();
        }}>
            <textarea
                placeholder="Enter your scenario..."
                rows="4"
                cols="50"
            />
            <button type="submit">Generate Comic</button>
        </form>
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
