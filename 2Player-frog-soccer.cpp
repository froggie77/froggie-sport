<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer Game</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1a5f23, #2d8a3a);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .game-container {
            background: #2d8a3a;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            border: 5px solid #1a4720;
            max-width: 800px;
            width: 100%;
        }
        
        .header {
            text-align: center;
            margin-bottom: 20px;
            color: white;
        }
        
        .header h1 {
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            margin-bottom: 10px;
        }
        
        .score-board {
            display: flex;
            justify-content: space-between;
            background: #1a4720;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 3px solid #f8b500;
        }
        
        .team {
            text-align: center;
            color: white;
            font-size: 1.2em;
        }
        
        .score {
            font-size: 3em;
            font-weight: bold;
            color: #f8b500;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        .game-field {
            position: relative;
            background: #4caf50;
            border: 5px solid white;
            border-radius: 10px;
            height: 500px;
            margin-bottom: 20px;
            overflow: hidden;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3);
        }
        
        .center-circle {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100px;
            height: 100px;
            border: 3px solid white;
            border-radius: 50%;
        }
        
        .center-spot {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
        }
        
        .goal {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 10px;
            height: 120px;
            background: #8B4513;
            border: 3px solid white;
        }
        
        .goal-left {
            left: 0;
        }
        
        .goal-right {
            right: 0;
        }
        
        .goal-net {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 30px;
            height: 140px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px dashed rgba(255, 255, 255, 0.3);
        }
        
        .goal-net-left {
            left: 10px;
        }
        
        .goal-net-right {
            right: 10px;
        }
        
        .player {
            position: absolute;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            transition: all 0.1s ease;
            z-index: 10;
        }
        
        .player-team-a {
            background: linear-gradient(45deg, #ff6b6b, #ff5252);
            border: 3px solid #c50e0e;
        }
        
        .player-team-b {
            background: linear-gradient(45deg, #4fc3f7, #29b6f6);
            border: 3px solid #0288d1;
        }
        
        .ball {
            position: absolute;
            width: 25px;
            height: 25px;
            background: white;
            border-radius: 50%;
            border: 2px solid #888;
            z-index: 5;
            transition: all 0.1s ease;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        }
        
        .controls {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .control-group {
            background: #1a4720;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #f8b500;
        }
        
        .control-group h3 {
            color: white;
            text-align: center;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        
        .keys {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 5px;
            justify-items: center;
        }
        
        .key {
            width: 50px;
            height: 50px;
            background: #333;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            font-weight: bold;
            border: 2px solid #666;
            box-shadow: 0 3px 0 #222;
        }
        
        .key.active {
            background: #f8b500;
            color: #333;
            transform: translateY(2px);
            box-shadow: 0 1px 0 #222;
        }
        
        .game-info {
            background: #1a4720;
            padding: 15px;
            border-radius: 10px;
            color: white;
            text-align: center;
            border: 2px solid #f8b500;
        }
        
        .reset-btn {
            background: #f8b500;
            color: #333;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.2s;
            box-shadow: 0 4px 0 #d89c00;
        }
        
        .reset-btn:hover {
            background: #ffc107;
            transform: translateY(-2px);
        }
        
        .reset-btn:active {
            transform: translateY(2px);
            box-shadow: 0 2px 0 #d89c00;
        }
        
        .message {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 20px 40px;
            border-radius: 10px;
            font-size: 2em;
            font-weight: bold;
            text-align: center;
            z-index: 100;
            display: none;
        }
        
        .half-line {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 3px;
            height: 100%;
            background: white;
        }
        
        .penalty-area {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 100px;
            height: 200px;
            border: 3px solid white;
        }
        
        .penalty-area-left {
            left: 0;
            border-right: none;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
        }
        
        .penalty-area-right {
            right: 0;
            border-left: none;
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <div class="header">
            <h1>⚽ Soccer Game ⚽</h1>
        </div>
        
        <div class="score-board">
            <div class="team">
                <div>Team Red</div>
                <div class="score" id="scoreA">0</div>
            </div>
            <div class="team">
                <div>Time: <span id="timer">90:00</span></div>
            </div>
            <div class="team">
                <div>Team Blue</div>
                <div class="score" id="scoreB">0</div>
            </div>
        </div>
        
        <div class="game-field" id="gameField">
            <!-- Field Markings -->
            <div class="center-circle"></div>
            <div class="center-spot"></div>
            <div class="half-line"></div>
            
            <!-- Goals -->
            <div class="goal goal-left"></div>
            <div class="goal goal-right"></div>
            <div class="goal-net goal-net-left"></div>
            <div class="goal-net goal-net-right"></div>
            
            <!-- Penalty Areas -->
            <div class="penalty-area penalty-area-left"></div>
            <div class="penalty-area penalty-area-right"></div>
            
            <!-- Players and Ball -->
            <div class="player player-team-a" id="playerA" style="left: 100px; top: 250px;"></div>
            <div class="player player-team-b" id="playerB" style="left: 700px; top: 250px;"></div>
            <div class="ball" id="ball" style="left: 400px; top: 250px;"></div>
            
            <!-- Goal Message -->
            <div class="message" id="goalMessage">GOAL!</div>
        </div>
        
        <div class="controls">
            <div class="control-group">
                <h3>Team Red Controls</h3>
                <div class="keys">
                    <div class="key" id="keyW">W</div>
                    <div class="key" id="keyA">A</div>
                    <div class="key" id="keyS">S</div>
                    <div class="key" id="keyD">D</div>
                    <div class="key" id="keySpace">SPACE</div>
                </div>
            </div>
            
            <div class="control-group">
                <h3>Team Blue Controls</h3>
                <div class="keys">
                    <div class="key" id="keyUp">↑</div>
                    <div class="key" id="keyLeft">←</div>
                    <div class="key" id="keyDown">↓</div>
                    <div class="key" id="keyRight">→</div>
                    <div class="key" id="keyEnter">ENTER</div>
                </div>
            </div>
        </div>
        
        <div class="game-info">
            <p>Shoot with SPACE (Red) or ENTER (Blue) | First to 5 goals wins!</p>
            <button class="reset-btn" id="resetBtn">Reset Game</button>
        </div>
    </div>

    <script>
        // Game elements
        const gameField = document.getElementById('gameField');
        const playerA = document.getElementById('playerA');
        const playerB = document.getElementById('playerB');
        const ball = document.getElementById('ball');
        const scoreA = document.getElementById('scoreA');
        const scoreB = document.getElementById('scoreB');
        const timer = document.getElementById('timer');
        const goalMessage = document.getElementById('goalMessage');
        const resetBtn = document.getElementById('resetBtn');
        
        // Key elements
        const keys = {
            w: document.getElementById('keyW'),
            a: document.getElementById('keyA'),
            s: document.getElementById('keyS'),
            d: document.getElementById('keyD'),
            space: document.getElementById('keySpace'),
            up: document.getElementById('keyUp'),
            left: document.getElementById('keyLeft'),
            down: document.getElementById('keyDown'),
            right: document.getElementById('keyRight'),
            enter: document.getElementById('keyEnter')
        };
        
        // Game state
        let gameState = {
            scoreA: 0,
            scoreB: 0,
            time: 90 * 60, // 90 minutes in seconds
            gameActive: true,
            ballOwner: null,
            keys: {
                w: false, a: false, s: false, d: false, space: false,
                up: false, left: false, down: false, right: false, enter: false
            }
        };
        
        // Player positions and velocities
        const players = {
            A: { x: 100, y: 250, vx: 0, vy: 0, speed: 3 },
            B: { x: 700, y: 250, vx: 0, vy: 0, speed: 3 }
        };
        
        // Ball properties
        const ballObj = {
            x: 400,
            y: 250,
            vx: 0,
            vy: 0,
            friction: 0.98,
            maxSpeed: 10
        };
        
        // Field boundaries
        const field = {
            left: 15,
            right: 785,
            top: 15,
            bottom: 485,
            goalLeft: { x: 0, y: 190, width: 10, height: 120 },
            goalRight: { x: 790, y: 190, width: 10, height: 120 }
        };
        
        // Initialize game
        function initGame() {
            resetPositions();
            updateGame();
            gameLoop();
        }
        
        // Reset positions
        function resetPositions() {
            players.A.x = 100;
            players.A.y = 250;
            players.B.x = 700;
            players.B.y = 250;
            ballObj.x = 400;
            ballObj.y = 250;
            ballObj.vx = 0;
            ballObj.vy = 0;
            gameState.ballOwner = null;
        }
        
        // Update game state
        function updateGame() {
            // Update player positions based on keys
            updatePlayerMovement();
            
            // Update ball physics
            updateBall();
            
            // Check for goals
            checkGoals();
            
            // Update display
            updateDisplay();
        }
        
        // Update player movement
        function updatePlayerMovement() {
            // Player A (WASD + Space)
            if (gameState.keys.w) players.A.vy = -players.A.speed;
            if (gameState.keys.s) players.A.vy = players.A.speed;
            if (gameState.keys.a) players.A.vx = -players.A.speed;
            if (gameState.keys.d) players.A.vx = players.A.speed;
            
            // Player B (Arrow keys + Enter)
            if (gameState.keys.up) players.B.vy = -players.B.speed;
            if (gameState.keys.down) players.B.vy = players.B.speed;
            if (gameState.keys.left) players.B.vx = -players.B.speed;
            if (gameState.keys.right) players.B.vx = players.B.speed;
            
            // Apply movement with boundaries
            players.A.x = Math.max(field.left, Math.min(field.right, players.A.x + players.A.vx));
            players.A.y = Math.max(field.top, Math.min(field.bottom, players.A.y + players.A.vy));
            
            players.B.x = Math.max(field.left, Math.min(field.right, players.B.x + players.B.vx));
            players.B.y = Math.max(field.top, Math.min(field.bottom, players.B.y + players.B.vy));
            
            // Reset velocities
            players.A.vx *= 0.8;
            players.A.vy *= 0.8;
            players.B.vx *= 0.8;
            players.B.vy *= 0.8;
            
            // Check ball possession
            checkBallPossession();
            
            // Shooting
            if (gameState.keys.space && gameState.ballOwner === 'A') {
                shootBall('A');
            }
            
            if (gameState.keys.enter && gameState.ballOwner === 'B') {
                shootBall('B');
            }
        }
        
        // Check ball possession
        function checkBallPossession() {
            const distA = Math.sqrt(
                Math.pow(players.A.x - ballObj.x, 2) + 
                Math.pow(players.A.y - ballObj.y, 2)
            );
            
            const distB = Math.sqrt(
                Math.pow(players.B.x - ballObj.x, 2) + 
                Math.pow(players.B.y - ballObj.y, 2)
            );
            
            if (distA < 30 && !gameState.ballOwner) {
                gameState.ballOwner = 'A';
                ballObj.vx = players.A.vx;
                ballObj.vy = players.A.vy;
            }
            
            if (distB < 30 && !gameState.ballOwner) {
                gameState.ballOwner = 'B';
                ballObj.vx = players.B.vx;
                ballObj.vy = players.B.vy;
            }
            
            // If player has ball, move it with them
            if (gameState.ballOwner === 'A') {
                ballObj.x = players.A.x + (players.A.vx > 0 ? 25 : -25);
                ballObj.y = players.A.y;
            }
            
            if (gameState.ballOwner === 'B') {
                ballObj.x = players.B.x + (players.B.vx > 0 ? -25 : 25);
                ballObj.y = players.B.y;
            }
        }
        
        // Shoot ball
        function shootBall(player) {
            const power = 8;
            if (player === 'A') {
                ballObj.vx = power * (players.A.vx > 0 ? 1 : -1);
                ballObj.vy = players.A.vy;
            } else {
                ballObj.vx = -power * (players.B.vx < 0 ? 1 : -1);
                ballObj.vy = players.B.vy;
            }
            gameState.ballOwner = null;
        }
        
        // Update ball physics
        function updateBall() {
            if (!gameState.ballOwner) {
                // Apply friction
                ballObj.vx *= ballObj.friction;
                ballObj.vy *= ballObj.friction;
                
                // Update position
                ballObj.x += ballObj.vx;
                ballObj.y += ballObj.vy;
                
                // Bounce off walls
                if (ballObj.x <= field.left || ballObj.x >= field.right) {
                    ballObj.vx = -ballObj.vx * 0.8;
                    ballObj.x = Math.max(field.left, Math.min(field.right, ballObj.x));
                }
                
                if (ballObj.y <= field.top || ballObj.y >= field.bottom) {
                    ballObj.vy = -ballObj.vy * 0.8;
                    ballObj.y = Math.max(field.top, Math.min(field.bottom, ballObj.y));
                }
                
                // Limit speed
                const speed = Math.sqrt(ballObj.vx * ballObj.vx + ballObj.vy * ballObj.vy);
                if (speed > ballObj.maxSpeed) {
                    ballObj.vx = (ballObj.vx / speed) * ballObj.maxSpeed;
                    ballObj.vy = (ballObj.vy / speed) * ballObj.maxSpeed;
                }
            }
        }
        
        // Check for goals
        function checkGoals() {
            // Goal for Team B (right goal)
            if (ballObj.x >= field.goalRight.x && 
                ballObj.y >= field.goalRight.y && 
                ballObj.y <= field.goalRight.y + field.goalRight.height) {
                gameState.scoreA++;
                showGoalMessage("Team Red Scores!");
            }
            
            // Goal for Team A (left goal)
            if (ballObj.x <= field.goalLeft.x + field.goalLeft.width && 
                ballObj.y >= field.goalLeft.y && 
                ballObj.y <= field.goalLeft.y + field.goalLeft.height) {
                gameState.scoreB++;
                showGoalMessage("Team Blue Scores!");
            }
            
            // Check for win
            if (gameState.scoreA >= 5) {
                showGoalMessage("Team Red Wins!");
                gameState.gameActive = false;
            } else if (gameState.scoreB >= 5) {
                showGoalMessage("Team Blue Wins!");
                gameState.gameActive = false;
            }
        }
        
        // Show goal message
        function showGoalMessage(text) {
            goalMessage.textContent = text;
            goalMessage.style.display = 'block';
            setTimeout(() => {
                goalMessage.style.display = 'none';
                if (gameState.gameActive) {
                    resetPositions();
                }
            }, 2000);
        }
        
        // Update display
        function updateDisplay() {
            // Update player positions
            playerA.style.left = players.A.x + 'px';
            playerA.style.top = players.A.y + 'px';
            playerB.style.left = players.B.x + 'px';
            playerB.style.top = players.B.y + 'px';
            
            // Update ball position
            ball.style.left = ballObj.x + 'px';
            ball.style.top = ballObj.y + 'px';
            
            // Update scores
            scoreA.textContent = gameState.scoreA;
            scoreB.textContent = gameState.scoreB;
            
            // Update timer
            const minutes = Math.floor(gameState.time / 60);
            const seconds = gameState.time % 60;
            timer.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        }
        
        // Game loop
        function gameLoop() {
            if (gameState.gameActive) {
                updateGame();
                gameState.time = Math.max(0, gameState.time - 1);
                
                if (gameState.time <= 0) {
                    gameState.gameActive = false;
                    if (gameState.scoreA > gameState.scoreB) {
                        showGoalMessage("Team Red Wins!");
                    } else if (gameState.scoreB > gameState.scoreA) {
                        showGoalMessage("Team Blue Wins!");
                    } else {
                        showGoalMessage("It's a Draw!");
                    }
                }
            }
            
            requestAnimationFrame(gameLoop);
        }
        
        // Event listeners for keyboard
        document.addEventListener('keydown', (e) => {
            switch(e.key.toLowerCase()) {
                case 'w': gameState.keys.w = true; keys.w.classList.add('active'); break;
                case 'a': gameState.keys.a = true; keys.a.classList.add('active'); break;
                case 's': gameState.keys.s = true; keys.s.classList.add('active'); break;
                case 'd': gameState.keys.d = true; keys.d.classList.add('active'); break;
                case ' ': gameState.keys.space = true; keys.space.classList.add('active'); e.preventDefault(); break;
                case 'arrowup': gameState.keys.up = true; keys.up.classList.add('active'); break;
                case 'arrowleft': gameState.keys.left = true; keys.left.classList.add('active'); break;
                case 'arrowdown': gameState.keys.down = true; keys.down.classList.add('active'); break;
                case 'arrowright': gameState.keys.right = true; keys.right.classList.add('active'); break;
                case 'enter': gameState.keys.enter = true; keys.enter.classList.add('active'); break;
            }
        });
        
        document.addEventListener('keyup', (e) => {
            switch(e.key.toLowerCase()) {
                case 'w': gameState.keys.w = false; keys.w.classList.remove('active'); break;
                case 'a': gameState.keys.a = false; keys.a.classList.remove('active'); break;
                case 's': gameState.keys.s = false; keys.s.classList.remove('active'); break;
                case 'd': gameState.keys.d = false; keys.d.classList.remove('active'); break;
                case ' ': gameState.keys.space = false; keys.space.classList.remove('active'); break;
                case 'arrowup': gameState.keys.up = false; keys.up.classList.remove('active'); break;
                case 'arrowleft': gameState.keys.left = false; keys.left.classList.remove('active'); break;
                case 'arrowdown': gameState.keys.down = false; keys.down.classList.remove('active'); break;
                case 'arrowright': gameState.keys.right = false; keys.right.classList.remove('active'); break;
                case 'enter': gameState.keys.enter = false; keys.enter.classList.remove('active'); break;
            }
        });
        
        // Reset button
        resetBtn.addEventListener('click', () => {
            gameState.scoreA = 0;
            gameState.scoreB = 0;
            gameState.time = 90 * 60;
            gameState.gameActive = true;
            resetPositions();
        });
        
        // Prevent space bar from scrolling page
        window.addEventListener('keydown', (e) => {
            if(e.key === ' ' && e.target === document.body) {
                e.preventDefault();
            }
        });
        
        // Start the game
        initGame();
    </script>
</body>
</html>