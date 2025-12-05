import React, { useState } from 'react';
import { Upload } from 'lucide-react';

const ForkliftPaperSolver = () => {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);
  const [grid, setGrid] = useState([]);
  const [part, setPart] = useState(1);

  const exampleInput = `..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.`;

  const solveForkliftProblem = (inputText, part2) => {
    const lines = inputText.trim().split('\n');
    const height = lines.length;
    const width = lines[0].length;
    
    // Parse the grid
    let gridData = lines.map(line => line.split(''));
    
    // Directions for 8 adjacent cells (including diagonals)
    const directions = [
      [-1, -1], [-1, 0], [-1, 1],
      [0, -1],           [0, 1],
      [1, -1],  [1, 0],  [1, 1]
    ];
    
    const findAccessible = (grid) => {
      const accessible = [];
      for (let row = 0; row < height; row++) {
        for (let col = 0; col < width; col++) {
          if (grid[row][col] === '@') {
            // Count adjacent paper rolls
            let adjacentCount = 0;
            
            for (const [dr, dc] of directions) {
              const newRow = row + dr;
              const newCol = col + dc;
              
              if (newRow >= 0 && newRow < height && 
                  newCol >= 0 && newCol < width && 
                  grid[newRow][newCol] === '@') {
                adjacentCount++;
              }
            }
            
            // Accessible if fewer than 4 adjacent rolls
            if (adjacentCount < 4) {
              accessible.push([row, col]);
            }
          }
        }
      }
      return accessible;
    };
    
    if (!part2) {
      // Part 1: Just count initially accessible rolls
      const accessible = findAccessible(gridData);
      const resultGrid = gridData.map(row => [...row]);
      accessible.forEach(([r, c]) => {
        resultGrid[r][c] = 'x';
      });
      
      setResult(accessible.length);
      setGrid(resultGrid);
    } else {
      // Part 2: Iteratively remove accessible rolls
      let totalRemoved = 0;
      let currentGrid = gridData.map(row => [...row]);
      
      while (true) {
        const accessible = findAccessible(currentGrid);
        if (accessible.length === 0) break;
        
        // Remove all accessible rolls
        accessible.forEach(([r, c]) => {
          currentGrid[r][c] = '.';
        });
        
        totalRemoved += accessible.length;
      }
      
      setResult(totalRemoved);
      setGrid(currentGrid);
    }
  };

  const handleSolve = () => {
    if (input.trim()) {
      solveForkliftProblem(input, part === 2);
    }
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target.result;
        setInput(text);
      };
      reader.readAsText(file);
    }
  };

  const useExample = () => {
    setInput(exampleInput);
    solveForkliftProblem(exampleInput, part === 2);
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-6 space-y-6">
      <div className="bg-green-50 border-2 border-green-600 rounded-lg p-6">
        <h1 className="text-3xl font-bold text-green-800 mb-2">
          🎄 Day 4: Printing Department
        </h1>
        <p className="text-gray-700 mb-4">
          Find paper rolls that can be accessed by forklifts (fewer than 4 adjacent rolls)
        </p>
        
        <div className="flex gap-4">
          <button
            onClick={() => setPart(1)}
            className={`px-4 py-2 rounded font-bold ${
              part === 1 
                ? 'bg-green-600 text-white' 
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            Part 1
          </button>
          <button
            onClick={() => setPart(2)}
            className={`px-4 py-2 rounded font-bold ${
              part === 2 
                ? 'bg-green-600 text-white' 
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            Part 2
          </button>
        </div>
      </div>

      <div className="bg-white border-2 border-gray-300 rounded-lg p-6 space-y-4">
        <div className="flex gap-4">
          <button
            onClick={useExample}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Use Example
          </button>
          
          <label className="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700 cursor-pointer flex items-center gap-2">
            <Upload size={20} />
            Upload Input
            <input
              type="file"
              accept=".txt"
              onChange={handleFileUpload}
              className="hidden"
            />
          </label>
        </div>

        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Paste your puzzle input here..."
          className="w-full h-48 p-3 border-2 border-gray-300 rounded font-mono text-sm"
        />

        <button
          onClick={handleSolve}
          className="w-full px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 font-bold"
        >
          Solve
        </button>
      </div>

      {result !== null && (
        <div className="bg-yellow-50 border-2 border-yellow-600 rounded-lg p-6">
          <h2 className="text-2xl font-bold text-yellow-800 mb-4">
            {part === 1 ? 'Part 1 Answer: ' : 'Part 2 Answer: '}
            {result} {part === 1 ? 'accessible rolls' : 'total rolls removed'}
          </h2>
          
          {grid.length > 0 && (
            <div className="mt-4">
              <h3 className="font-bold mb-2">
                {part === 1 ? 'Visualization (x = accessible):' : 'Final state after all removals:'}
              </h3>
              <div className="bg-gray-900 p-4 rounded overflow-auto">
                <pre className="font-mono text-sm text-green-400">
                  {grid.map((row, i) => (
                    <div key={i}>
                      {row.map((cell, j) => (
                        <span
                          key={j}
                          className={cell === 'x' ? 'text-yellow-300 font-bold' : ''}
                        >
                          {cell}
                        </span>
                      ))}
                    </div>
                  ))}
                </pre>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ForkliftPaperSolver;