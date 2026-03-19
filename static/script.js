async function fetchTeams(year) {
  const teamList = document.getElementById("teamList");
  const teamsError = document.getElementById("teamsError");

  teamList.innerHTML = "";
  teamsError.hidden = true;

  try {
    const res = await fetch(`/teams?year=${year}`);
    if (!res.ok) {
      throw new Error(`Server returned ${res.status}`);
    }

    const data = await res.json();
    const teams = Array.isArray(data.teams) ? data.teams : [];

    if (teams.length === 0) {
      teamsError.hidden = false;
      teamsError.textContent = "No teams found for this season.";
      return;
    }

    teams.forEach(({ teamID, name }) => {
      const li = document.createElement("li");
      li.textContent = name ? `${name} (${teamID})` : teamID;
      teamList.appendChild(li);
    });
  } catch (err) {
    console.error(err);
    teamsError.hidden = false;
    teamsError.textContent = "Unable to load teams. Try again later.";
  }
}

async function fetchYears() {
  const yearSelect = document.getElementById("yearSelect");
  const selected = document.getElementById("selectedYear");
  const error = document.getElementById("error");

  try {
    const res = await fetch("/years");
    if (!res.ok) {
      throw new Error(`Server returned ${res.status}`);
    }

    const data = await res.json();
    const years = Array.isArray(data.years) ? data.years : [];

    yearSelect.innerHTML = "";
    years.forEach((year) => {
      const option = document.createElement("option");
      option.value = year;
      option.textContent = year;
      yearSelect.appendChild(option);
    });

    if (years.length > 0) {
      yearSelect.disabled = false;
      selected.textContent = `Selected year: ${years[0]}`;
      await fetchTeams(years[0]);
    } else {
      yearSelect.disabled = true;
      selected.textContent = "No years available";
    }

    yearSelect.addEventListener("change", async () => {
      selected.textContent = `Selected year: ${yearSelect.value}`;
      await fetchTeams(yearSelect.value);
    });
  } catch (err) {
    console.error(err);
    error.hidden = false;
    error.textContent = "Unable to load years. Try again later.";
  }
}

window.addEventListener("DOMContentLoaded", fetchYears);
