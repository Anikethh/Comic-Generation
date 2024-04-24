import React, { useState } from 'react';
import ScenarioForm from './components/ScenarioForm';
import ComicGrid from './components/ComicGrid';
import axios from 'axios';
import './App.css';

function App() {
  const [panels, setPanels] = useState(Array.from({ length: 6 }, () => null));  // Initialize with nulls
  const [isLoading, setIsLoading] = useState(false);

  const handleGenerateClick = async (prompt) => {
    setIsLoading(true);
    try {
        const response = await axios.post('/generate-image', { prompt });
        setPanels(response.data); // response.data should be the array of paths
    } catch (error) {
        console.error('Error fetching images:', error);
        // Optionally keep the old panels or reset
    } finally {
        setIsLoading(false);
    }
  };

  return (
      <div className="App">
          <div className="sidebar">
            <div className="sidebar-logo">
                <img src="Media/VectorLogo.svg" alt="Logo" />
            </div>
            <div className="sidebar-icon">
                <img src="Media/mingcute_layout-lineLayout1.svg" alt="Layout 1" />
            </div>
            <div className="sidebar-icon">
                <img src="Media/mingcute_layout-lineLayout2.svg" alt="Layout 2" />
            </div>
            <div className="sidebar-icon">
                <img src="Media/mingcute_layout-lineLayout3.svg" alt="Layout 3" />
            </div>
            <div className="sidebar-icon">
                <img src="Media/mingcute_layout-lineLayout4.svg" alt="Layout 4" />
            </div>
          </div>
          <div className="content">
              <div className="left-container">
                  <h1 className="title">Comic Generator</h1>
                  <ScenarioForm onGenerate={handleGenerateClick} />
              </div>
              <div className="right-container">
                  <ComicGrid panels={panels} isLoading={isLoading} />
              </div>
          </div>
      </div>
  );
}

export default App;





// import React, { useState } from 'react';
// import ScenarioForm from './components/ScenarioForm';
// import ComicGrid from './components/ComicGrid';
// import './App.css';  // Make sure you have some global styles set up here

// function App() {
//     const [panels, setPanels] = useState([]);  // This will store the URLs to the images

//     const handleScenarioSubmit = (scenario) => {
//         // Here you would typically make an API call or some other process to fetch the images
//         // For now, let's simulate with placeholder data
//         const newPanels = [
//             '/path/to/image1.png',
//             '/path/to/image2.png',
//             '/path/to/image3.png',
//             '/path/to/image4.png',
//             '/path/to/image5.png',
//             '/path/to/image6.png'
//         ];
//         setPanels(newPanels);  // Update state with new panels
//     };

//     return (
//         <div className="App">
//             <header className="App-header">
//                 <h1>Comic Generator</h1>
//             </header>
//             <ScenarioForm onSubmitScenario={handleScenarioSubmit} />
//             <ComicGrid panels={panels} />
//         </div>
//     );
// }

// const handleScenarioSubmit = (panels) => {
//     setPanels(panels); // Update the state with the new panels
// };

// export default App;
