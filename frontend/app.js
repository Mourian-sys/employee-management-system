async function loadEmployees() {

    const response =
        await fetch("http://localhost:5000/employees");

    const data = await response.json();

    document.getElementById("output").innerHTML =
        JSON.stringify(data, null, 2);
}
