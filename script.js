const startBtn = document.getElementById('startBtn');
const restartBtn = document.getElementById('restartBtn');
const gameOverScreen = document.getElementById('gameOverScreen');
const plane = document.getElementById('plane');
const player = document.getElementById('player');
const parachute = document.getElementById('parachute');
const gunCrate = document.getElementById('gunCrate');
const dropZone = document.getElementById('dropZone');
const statusNote = document.getElementById('statusNote');
const gameCanvasWrapper = document.getElementById('gameCanvasWrapper');
const gun = document.getElementById('gun');
const gun2 = document.getElementById('gun2');
const player2 = document.getElementById('player2');
const miniMapCanvas = document.getElementById('miniMapCanvas');
const miniPlayer = document.getElementById('miniPlayer');

let running = false;
let timerId = null;

function resetCharacters() {
  plane.className = 'plane';
  player.className = 'player';
  parachute.className = 'parachute';
  gunCrate.className = 'gun-crate';
  dropZone.className = 'drop-zone';
  statusNote.textContent = 'Ready. Start karo.';
  if (gun) gun.className = 'gun';
  if (player2) player2.className = 'player player2';
  if (gun2) gun2.className = 'gun';
}

function resetGame() {
  running = false;
  clearTimeout(timerId);
  resetCharacters();
  gameOverScreen.classList.remove('visible');
  startBtn.textContent = 'Start';
}

function gameOver() {
  running = false;
  clearTimeout(timerId);
  gameOverScreen.classList.add('visible');
  startBtn.textContent = 'Phir se';
  statusNote.textContent = 'Mission failed. Restart karo.';
}

function startPlaneRun() {
  dropZone.classList.add('active');
  statusNote.textContent = 'Plane entry. Drop zone secure.';
  plane.classList.add('in-flight');

  timerId = setTimeout(() => {
    releasePlayer();
  }, 2400);
}

function releasePlayer() {
  player.classList.add('fall');
  statusNote.textContent = 'Player drop kar raha hai. Parachute deploy.';

  timerId = setTimeout(() => {
    parachute.classList.add('open');
  }, 500);

  timerId = setTimeout(() => {
    player.classList.add('landed');
    statusNote.textContent = 'Landing complete. Crate approach.';
  }, 2000);

  timerId = setTimeout(() => {
    dropZone.classList.remove('active');
    player.classList.remove('fall');
    spawnCrate();
  }, 2200);
}

function spawnCrate() {
  gunCrate.classList.add('visible', 'glow');
  statusNote.textContent = 'Gun crate arrive hua. Check karo.';

  timerId = setTimeout(() => {
    player.classList.add('walk');
    statusNote.textContent = 'Player crate ki taraf badh raha hai.';
  }, 1200);

  timerId = setTimeout(() => {
    pickGun();
  }, 2300);
}

function pickGun() {
  gunCrate.classList.remove('visible', 'glow');
  player.classList.add('armed');
  player.style.transform = 'translateX(80%)';
  statusNote.textContent = 'Gun pickup complete. Ready to engage.';
  if (gun) gun.classList.add('visible');
  // For local 2-player: arm player2 as well when crate is taken
  if (player2) player2.classList.add('armed');
  if (gun2) gun2.classList.add('visible');
}

function startGame() {
  if (running) return;
  running = true;
  startBtn.textContent = 'Running...';
  resetCharacters();
  setTimeout(startPlaneRun, 120);
}

function handleShoot() {
  if (!running) return;
  if (!player.classList.contains('armed')) {
    statusNote.textContent = 'Abhi weapon nahi hai. Pehle pickup karo.';
    return;
  }
  statusNote.textContent = 'Shot fired. Nice hit.';
  spawnBullet('p1');
  if (socket) socket.emit('shoot', { owner: 'p1' });
}
// owner: 'p1' or 'p2'
function spawnBullet(owner = 'p1') {
  if (!gameCanvasWrapper) return;

  const ownerGun = owner === 'p2' ? gun2 : (owner === 'p1' ? gun : null);

  const bullet = document.createElement('div');
  bullet.className = 'bullet';
  bullet.dataset.owner = owner;
  gameCanvasWrapper.appendChild(bullet);

  let wrapperRect = gameCanvasWrapper.getBoundingClientRect();
  let x, y;

  if (ownerGun) {
    const gunRect = ownerGun.getBoundingClientRect();
    x = gunRect.left - wrapperRect.left + gunRect.width / 2;
    y = gunRect.top - wrapperRect.top + gunRect.height / 2 - 2;
    ownerGun.classList.add('shoot');
    setTimeout(() => ownerGun.classList.remove('shoot'), 120);
  } else {
    // remote or fallback: spawn from left edge center
    x = 16;
    y = wrapperRect.height / 2;
  }

  bullet.style.left = x + 'px';
  bullet.style.top = y + 'px';
  bullet.style.opacity = '1';

  const speed = owner === 'p2' ? 16 : 18;

  function step() {
    wrapperRect = gameCanvasWrapper.getBoundingClientRect();
    x += speed;
    y -= 0.18 * (speed / 18);

    bullet.style.left = x + 'px';
    bullet.style.top = y + 'px';

    // targets: p1 and p2
    const targets = [ {el: player, id: 'p1'}, {el: player2, id: 'p2'} ];
    for (const t of targets) {
      if (!t.el) continue;
      // owner should not hit itself
      if (owner === t.id) continue;
      if (t.el.classList.contains('dead')) continue;
      const bRect = bullet.getBoundingClientRect();
      const pRect = t.el.getBoundingClientRect();
      if (!(bRect.right < pRect.left || bRect.left > pRect.right || bRect.bottom < pRect.top || bRect.top > pRect.bottom)) {
        t.el.classList.add('dead');
        statusNote.textContent = `${t.id} was shot by ${owner}!`;
        bullet.remove();
        setTimeout(() => {
          t.el.classList.remove('dead');
          statusNote.textContent = 'Respawned.';
        }, 2000);
        return;
      }
    }

    if (x > wrapperRect.width + 80 || y < -120) { bullet.remove(); return; }
    requestAnimationFrame(step);
  }

  requestAnimationFrame(step);
}

// Minimal Socket.IO client hooks for online multiplayer (optional)
let socket = null;
try {
  if (typeof io !== 'undefined') {
    socket = io();
    socket.on('connect', () => { statusNote.textContent = 'Online: connected'; });
    socket.on('shoot', (data) => {
      // remote player fired — spawn a remote bullet for now
      spawnBullet('remote');
    });
  }
} catch (err) {
  // ignore if socket.io not available (file:// open)
}

// Minimap: map player's position inside the game wrapper to the minimap canvas
function updateMinimapPosition() {
  if (!miniMapCanvas || !miniPlayer || !player) return;
  const wrapperRect = gameCanvasWrapper.getBoundingClientRect();
  const playerRect = player.getBoundingClientRect();

  const playerCenterX = playerRect.left + playerRect.width / 2 - wrapperRect.left;
  const playerCenterY = playerRect.top + playerRect.height / 2 - wrapperRect.top;

  const relX = playerCenterX / wrapperRect.width;
  const relY = playerCenterY / wrapperRect.height;

  const mapW = miniMapCanvas.clientWidth;
  const mapH = miniMapCanvas.clientHeight;

  const px = Math.max(6, Math.min(mapW - 6, Math.round(relX * mapW)));
  const py = Math.max(6, Math.min(mapH - 6, Math.round(relY * mapH)));

  miniPlayer.style.left = px + 'px';
  miniPlayer.style.top = py + 'px';
}

// Continuous loop to keep minimap in sync
(function minimapLoop() {
  updateMinimapPosition();
  requestAnimationFrame(minimapLoop);
})();

startBtn.addEventListener('click', () => {
  if (!running) {
    startGame();
  }
});

restartBtn.addEventListener('click', () => {
  resetGame();
  startGame();
});

gameCanvasWrapper.addEventListener('click', handleShoot);

document.addEventListener('keydown', (event) => {
  if (event.code === 'Space') {
    handleShoot();
  }
});

// Local PvP: Enter to shoot for player2
document.addEventListener('keydown', (event) => {
  if (!running) return;
  if (event.code === 'Enter') {
    if (!player2 || !player2.classList.contains('armed')) {
      statusNote.textContent = 'Player2 has no weapon yet.';
      return;
    }
    spawnBullet('p2');
    if (socket) socket.emit('shoot', { owner: 'p2' });
  }
});

resetGame();
