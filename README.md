![image](https://www.riotgames.com/darkroom/1440/a4e88f6b04bf83f1c417e87292b85606:b62ff9b783f3dd26a6321e1440efe13b/riot-games-the-team-behind-worlds-2022-esports-broadcast-league-of-legends.png)

# LOL Esports Datalake

The LOL Esports Datalake project aims to gather comprehensive information about games, teams, tournaments, and other relevant data from various leagues including CBLOL, LEC, LCS, and others. This data is then fed into a datalake for further analysis and utilization.

## Getting Started

### Prerequisites

- Python 3.11
- Ensure you have pip installed

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/lol-esports-datalake.git
   ```

2. Navigate to the project directory:

   ```bash
   cd lol-esports-datalake
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the Database:

   - The default database is SQLite but can be any SQL database. You need to specify the database path in `src/model/s.py`.

## Starting the Datalake

### Initialization

To start the datalake, follow these steps:

1. Initialize the datalake:

   ```bash
   python start.py
   ```

   This command initializes the datalake and creates the necessary tables for leagues and tournaments.

### Populating Data

To populate the datalake with data:

1. Run the main script:

   ```bash
   python main.py
   ```

   This script allows you to choose a specific tournament and retrieves all matches/games along with their frames (specific moments of the game).

## Usage

Once the datalake is populated with data, you can perform various analyses, generate insights, and derive valuable information about esports tournaments, teams, and games.

## Contributing

Contributions to the project are welcome! Feel free to submit pull requests, report issues, or suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to Riot Games for providing access to the API and supporting the development of esports analytics.

---

Feel free to customize and expand this README further to include additional details, instructions, or acknowledgments as needed for your project.

