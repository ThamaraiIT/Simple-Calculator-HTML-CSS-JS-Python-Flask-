function appendValue(value) {
  document.getElementById("display").value += value;
}

function clearDisplay() {
  document.getElementById("display").value = '';
}

async function calculateResult() {
  const expression = document.getElementById("display").value;
  const response = await fetch("/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ expression })
  });
  const data = await response.json();
  document.getElementById("display").value = data.result;
}
