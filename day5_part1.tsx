import React, { useState } from 'react';
import { CheckCircle, XCircle, Upload } from 'lucide-react';

export default function IngredientChecker() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);
  const [details, setDetails] = useState([]);

  const exampleInput = `3-5
10-14
16-20
12-18

1
5
8
11
17
32`;

  const parseAndCheck = (text) => {
    const lines = text.trim().split('\n');
    
    // Find the blank line that separates ranges from IDs
    const blankLineIndex = lines.findIndex(line => line.trim() === '');
    
    if (blankLineIndex === -1) {
      alert('Invalid input: no blank line found separating ranges from IDs');
      return;
    }
    
    // Parse fresh ranges
    const rangeLines = lines.slice(0, blankLineIndex);
    const ranges = rangeLines.map(line => {
      const [start, end] = line.split('-').map(Number);
      return { start, end };
    });
    
    // Parse available ingredient IDs
    const idLines = lines.slice(blankLineIndex + 1);
    const ids = idLines
      .filter(line => line.trim() !== '')
      .map(Number);
    
    // Check each ID
    const checkResults = ids.map(id => {
      const isFresh = ranges.some(range => id >= range.start && id <= range.end);
      const matchingRanges = ranges
        .filter(range => id >= range.start && id <= range.end)
        .map(r => `${r.start}-${r.end}`);
      
      return {
        id,
        isFresh,
        matchingRanges
      };
    });
    
    const freshCount = checkResults.filter(r => r.isFresh).length;
    
    setResult(freshCount);
    setDetails(checkResults);
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target.result;
        setInput(text);
        parseAndCheck(text);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-red-50 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <h1 className="text-3xl font-bold text-green-800 mb-2">
            🎄 Cafeteria Ingredient Checker
          </h1>
          <p className="text-gray-600 mb-4">
            Day 5: Determine which ingredients are fresh based on ID ranges
          </p>
          
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Paste your puzzle input or upload a file:
            </label>
            <textarea
              className="w-full h-48 p-3 border border-gray-300 rounded-lg font-mono text-sm"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder={exampleInput}
            />
          </div>
          
          <div className="flex gap-3 mb-4">
            <button
              onClick={() => parseAndCheck(input)}
              className="flex-1 bg-green-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-700 transition"
            >
              Check Ingredients
            </button>
            
            <button
              onClick={() => {
                setInput(exampleInput);
                parseAndCheck(exampleInput);
              }}
              className="flex-1 bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition"
            >
              Try Example
            </button>
            
            <label className="flex-1 bg-gray-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-gray-700 transition cursor-pointer text-center">
              <Upload className="inline-block mr-2" size={20} />
              Upload File
              <input
                type="file"
                onChange={handleFileUpload}
                className="hidden"
                accept=".txt"
              />
            </label>
          </div>
          
          {result !== null && (
            <div className="bg-green-100 border-2 border-green-600 rounded-lg p-6 text-center">
              <p className="text-lg text-gray-700 mb-2">Fresh Ingredients Found:</p>
              <p className="text-5xl font-bold text-green-800">{result}</p>
            </div>
          )}
        </div>
        
        {details.length > 0 && (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">
              Ingredient Details
            </h2>
            <div className="space-y-2">
              {details.map((item, index) => (
                <div
                  key={index}
                  className={`flex items-center justify-between p-3 rounded-lg ${
                    item.isFresh ? 'bg-green-50' : 'bg-red-50'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    {item.isFresh ? (
                      <CheckCircle className="text-green-600" size={24} />
                    ) : (
                      <XCircle className="text-red-600" size={24} />
                    )}
                    <span className="font-mono font-semibold text-lg">
                      ID {item.id}
                    </span>
                  </div>
                  <div className="text-right">
                    {item.isFresh ? (
                      <span className="text-green-700">
                        Fresh (ranges: {item.matchingRanges.join(', ')})
                      </span>
                    ) : (
                      <span className="text-red-700">Spoiled</span>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}