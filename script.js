// Replace <USERNAME> and <REPO> with your actual GitHub username and repository name
const csvUrl = "https://raw.githubusercontent.com/rahmafallous2/ebay-tech-deals/main/cleaned_ebay_deals.csv";

async function fetchCsvData() {
  try {
    const response = await fetch(csvUrl);
    if (!response.ok) throw new Error("Network response was not ok " + response.statusText);
    const csvText = await response.text();

    // PapaParse handles multi-line cells and commas inside quotes
    const parsed = Papa.parse(csvText, { header: true, skipEmptyLines: true });
    
    // Remove rows that are mostly empty or incomplete
    const cleanData = parsed.data.filter(row => row.title || row.price || row.item_url);
    
    createTable(cleanData);
  } catch (error) {
    console.error("Error fetching CSV data:", error);
    document.getElementById("data-container").innerHTML = `<p style="color:red;">Failed to load data. Check console.</p>`;
  }
}

function createTable(data) {
  let html = "<table><thead><tr>";
  Object.keys(data[0]).forEach(header => { html += `<th>${header}</th>`; });
  html += "</tr></thead><tbody>";

  data.forEach(row => {
    html += "<tr>";
    Object.values(row).forEach(cell => { html += `<td>${cell || ''}</td>`; });
    html += "</tr>";
  });

  html += "</tbody></table>";
  document.getElementById("data-container").innerHTML = html;
}

// Basic styling
const style = document.createElement("style");
style.innerHTML = `
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #444; padding: 6px; text-align: left; }
  th { background-color: #f2f2f2; }
  tbody tr:nth-child(even) { background-color: #fafafa; }
`;
document.head.appendChild(style);

window.addEventListener("DOMContentLoaded", fetchCsvData);