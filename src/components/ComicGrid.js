import React from 'react';

function ComicGrid({ panels }) {
    return (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
            {panels.map((panel, index) => (
                <img key={index} src={panel} alt={`Panel ${index + 1}`} style={{ width: '100%' }} />
            ))}
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
