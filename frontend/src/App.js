// import { ImageUpload } from "./home";

// function App() {
//   return <ImageUpload />;
// }

// export default App;

import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ImageUpload_Potato } from "./home";
import { ImageUpload_Tomato } from "./home";
import SelectPrediction from './SelectPrediction';

function App() {
  const [predictionType, setPredictionType] = useState('');

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={<SelectPrediction setPredictionType={setPredictionType} />}
        />
        <Route
          path="/potato_predict"
          element={<ImageUpload_Potato />}
        />
        <Route
          path="/tomato_predict"
          element={<ImageUpload_Tomato />}
        />
      </Routes>
    </Router>
  );
}

export default App;