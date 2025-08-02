// encrypt-books.js
const fs = require("fs");
const CryptoJS = require("crypto-js");

// === CONFIG ===
const PASSWORD = "books"; // universal password
const INPUT_FILE = "books_content.html";
const OUTPUT_FILE = "books_secret.enc.js";

// === READ HTML CONTENT ===
const htmlContent = fs.readFileSync(INPUT_FILE, "utf8");

// === ENCRYPT CONTENT ===
const encrypted = CryptoJS.AES.encrypt(htmlContent, PASSWORD).toString();

// === WRITE TO JS FILE ===
const jsContent = `const encryptedHTML = "${encrypted}";`;

fs.writeFileSync(OUTPUT_FILE, jsContent);

console.log(`Encrypted content written to ${OUTPUT_FILE}`);
