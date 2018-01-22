function Encrypt(){
	cipherFunction = document.getElementById("cipher").value;
	plainText = document.getElementById("plainText").value.toLowerCase();
	key = document.getElementById("key").value;
	if(cipherFunction == "caeser"){
		caeserEncrypt(plainText, parseInt(key));
	}
}

function caeserEncrypt(text, shift){
	if(text.length < 1){
		alert("There was no plain text inserted.");
	}
	else {
		result = "";
		var re = /[a-z]/;
		for(i=0; i < text.length; i++){
			if(re.test(text.charAt(i))){
				result += String.fromCharCode((text.charCodeAt(i) - 97 + shift)%26 + 97);
			} else {
				result += text.charAt(i);
			}
		}
		document.getElementById("cipherText").innerHTML = result;
	}
}

// function Decrypt(){
// 	cipherFunction = document.getElementById("cipher").value;
// 	plainText = document.getElementById("plainText").value.toLowerCase();
// 	key = document.getElementById("key").value;
// 	if(cipherFunction == "caeser"){
// 		caeserDecrypt(plainText, key);
// 	}
// }
//
// function caeserDecrypt(plainText, key){
// 	if(cipherText.length < 1){ alert("please enter some ciphertext (letters only)"); return; }
// 	 var shift = parseInt(document.getElementById("key").value);
// 	 plaintext = "";    var re = /[a-z]/;
// 	 for(i=0; i<ciphertext.length; i++){
// 			 if(re.test(ciphertext.charAt(i))) plaintext += String.fromCharCode((ciphertext.charCodeAt(i) - 97 + 26 - shift)%26 + 97);
// 			 else plaintext += ciphertext.charAt(i);
// 	 }
// 	 document.getElementById("p").value = plaintext;
// }
