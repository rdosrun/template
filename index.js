// Import necessary modules
const express = require('express');
const path = require('path');

// Create an instance of an Express app
const app = express();

// Middleware to parse JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


// Serve static files (e.g., CSS, JavaScript, images) from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to serve the home page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.get('/views/:page', (req, res) => {
    const page = req.params.page;
    const filePath = path.join(__dirname, 'views', `${page}.html`);
    console.log(filePath);
    res.sendFile(filePath, (err) => {
        if (err) {
            res.status(404).send('Page not found');
        }
    });
});

// Example API endpoint
app.get('/api/greeting', (req, res) => {
    res.json({ message: 'Hello, world!' });
});

// API endpoint to handle POST requests
app.post('/api/echo', (req, res) => {
    const { input } = req.body;
    res.json({ echoedInput: input });
});

// Route for unauthorized users
app.get('/unauthorized', (req, res) => {
    res.status(401).json({ error: 'Unauthorized access' });
});

// Handle 404 errors for unrecognized routes
app.use((req, res) => {
    res.status(404).send('Page not found');
});

// Start the server
const PORT = 4000;
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server is running on http://localhost:${PORT}`);
    console.log(`Accessible on the LAN at http://<your-lan-ip>:${PORT}`);
});

