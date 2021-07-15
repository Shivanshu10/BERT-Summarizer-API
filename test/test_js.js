async function getSummary(text, url) {
    var params={
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "selection": text})
    };
    var resp=await fetch(url, params);
    console.log(resp);
    return resp.json();
};
var resp=await getSummary("HELLO WORLD", "http://127.0.0.1:5000/");
console.log(resp);