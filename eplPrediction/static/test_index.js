const teams = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton",
    "Burnley",
    "Cardiff",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Huddersfield",
    "Leeds",
    "Leicester",
    "Liverpool",
    "Man City",
    "Man United",
    "Newcastle",
    "Norwich",
    "Sheffield United",
    "Southampton",
    "Stoke",
    "Swansea",
    "Tottenham",
    "Watford",
    "West Brom",
    "West Ham",
    "Wolves",
  ];

  const inputValues = {};
  document.addEventListener("DOMContentLoaded", async () => {
    const element = document.getElementById("teams1");
    const element1 = document.getElementById("teams2");
    teams.forEach((team) => {
      const newElement = document.createElement("option");
      // newElement.className="select-item";
      newElement.value = team;
      const newElement1 = newElement.cloneNode();
      element.appendChild(newElement);
      element1.appendChild(newElement1);
    });
  
  });
  
  const validateForm = () => {
    document.getElementsByName("team1").forEach((e, i) => {
      inputValues[`value${i}`] = e.value;
    });
    document.getElementsByName("team2").forEach((e, i) => {
        inputValues[`valuee${i}`] = e.value;
      });
    if(!inputValues["value0"]){
      return 
    }
    if(!inputValues["valuee0"]){
      return 
    }
    if(inputValues["value0"] === inputValues["valuee0"]){
      return 
    }
    document.getElementById('odds').disabled = false;
  }
  