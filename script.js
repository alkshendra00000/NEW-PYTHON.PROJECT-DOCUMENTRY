let userScore = 0;
let computerScore = 0;


const choices = document.querySelectorAll(".choice");

const msg = document.querySelector("#msg");

const userScorePara = document.querySelector("#user-score");
const computerScorePara = document.querySelector("#comp-score");
const playAgainButton = document.querySelector("#play-again");




const generateComputerChoice = () => {
    const options = ["rock", "paper", "scissors"];
    const randIdx = Math.floor(Math.random() * options.length);
    return options[randIdx];
};

const drawGame = () => {
    msg.textContent = "It's a draw. Play again.";
    msg.style.backgroundColor = "#2563eb";
};

const resetGame = () => {
    userScore = 0;
    computerScore = 0;
    userScorePara.textContent = userScore;
    computerScorePara.textContent = computerScore;
    msg.textContent = "Choose your move";
    msg.style.backgroundColor = "#081b31";
};

const showWinner = (userWin, userChoice, computerChoice) => {
    if (userWin) {
        userScore++;
        userScorePara.textContent = userScore;
        msg.textContent = `You win! ${userChoice} beats ${computerChoice}.`;
        msg.style.backgroundColor = "#15803d";
    } else {
        computerScore++;
        computerScorePara.textContent = computerScore;
        msg.textContent = `You lose! ${computerChoice} beats ${userChoice}.`;
        msg.style.backgroundColor = "#dc2626";
    }
};
const playGame = (userChoice) => {
    const computerChoice = generateComputerChoice();

    if (userChoice === computerChoice) {
        drawGame();
        return;
    }

    const userWin =
        (userChoice === "rock" && computerChoice === "scissors") ||
        (userChoice === "paper" && computerChoice === "rock") ||
        (userChoice === "scissors" && computerChoice === "paper");

    showWinner(userWin, userChoice, computerChoice);

};

choices.forEach((choice) => {
    choice.addEventListener("click", () =>{
        playGame(choice.id);

    });

});

playAgainButton.addEventListener("click", resetGame);