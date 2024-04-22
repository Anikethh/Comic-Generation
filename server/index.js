const express = require('express');
const app = express();
const PORT = 3001;

app.use('/output', express.static('../output'));

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});


// const express = require('express');
// const { exec } = require('child_process');
// const app = express();
// const PORT = 3001;

// app.use(express.json()); 

// app.post('/generate', (req, res) => {
//     const { scenario } = req.body;
//     exec(`python ../kartoon.py "${scenario.replace(/"/g, '\\"')}"`, (error, stdout, stderr) => {
//         if (error) {
//             console.error(`exec error: ${error}`);
//             return res.status(500).send('Error generating comic');
//         }
//         // Assuming the Python script saves images and you know the filenames
//         const panels = Array.from({ length: 6 }, (_, i) => `/output/panel-${i + 1}.png`);
//         res.json({ panels });
//     });
// });

// app.listen(PORT, () => {
//     console.log(`Server running on http://localhost:${PORT}`);
// });
