import React from 'react';

function ComicGrid({ panels }) {
    // Calculate the aspect ratio based on 1024x1152
    const aspectRatio = 1024 / 1152; // Width / Height

    return (
        <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(2, 1fr)', // Two columns
            gap: '10px',
            width: '100%', // Ensure the grid takes full width of its container
            padding: '20px',
            boxSizing: 'border-box', // Include padding in the width calculation
        }}>
            {panels.length > 0 ? (
                panels?.map((panel, index) => (
                    <div key={index} style={{
                        width: '100%', // Full width of the grid cell
                        paddingTop: `${100 / aspectRatio}%`, // Padding-top based on aspect ratio
                        position: 'relative', // Container for the image
                    }}>
                        <img src={panel} alt={`Panel ${index + 1}`}
                             style={{
                                 position: 'absolute',
                                 top: 0,
                                 left: 0,
                                 width: '100%', // Full width of the container
                                 height: '100%', // Full height of the container
                                 objectFit: 'cover', // Cover the area without distortion
                                 borderRadius: '8px', // Rounded corners
                             }}
                        />
                    </div>
                ))
            ) : (
                Array.from({ length: 6 }).map((_, index) => (
                    <div key={index} style={{
                        backgroundColor: '#333', // Dark background for placeholders
                        border: '2px solid #444', // Slightly lighter border
                        borderRadius: '8px', // Rounded corners
                        width: '100%', // Full width of the grid cell
                        paddingTop: `${100 / aspectRatio}%`, // Padding-top based on aspect ratio
                        position: 'relative', // Needed for absolute positioning of children
                    }}></div>
                ))
            )}
        </div>
    );
}

export default ComicGrid;




// import React from 'react';

// function ComicGrid({ panels }) {
//   return (
//     <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
//       {panels.map((panel, index) => (
//         <img key={index} src={panel} alt={`Panel ${index + 1}`} style={{ width: '100%' }} />
//       ))}
//     </div>
//   );
// }

// export default ComicGrid;
