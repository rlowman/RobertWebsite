function encrypt(){
	var cipherFunction = document.getElementById("cipher").value;
	var plainText = document.getElementById("plainText").value.toLowerCase();
	var cipherText = plainText
	if(cipherFunction == "caeser"){
		cipherText = caeserEncrypt(plainText);
	}
	else if(cipherFunction == "otp"){
		cipherText = otpEncrypt(plainText);
	}
	document.getElementById("cipherText").value = cipherText;
}

function caeserEncrypt(text){
	if(text.length < 1){
		alert("There was no plain text inserted.");
	}
	else {
		result = "";
		var re = /[a-z]/;
		var shift = parseInt(document.getElementById("shift").value);
		for(i=0; i < text.length; i++){
			if(re.test(text.charAt(i))){
				result += String.fromCharCode((text.charCodeAt(i) - 97 + shift)%26 + 97);
			} else {
				result += text.charAt(i);
			}
		}
		return result;
	}
}

function otpEncrypt(text){
	if(text.length < 1){
		alert("There was no plain text inserted.");
	}
	else {
		var key = document.getElementById("key").value.toLowerCase();
		var result = "";
		var re = /[a-z]/;
		var keyIndex = 0;
		for(i=0; i < text.length; i++){
			if(re.test(text.charAt(i))){
			  result += String.fromCharCode(((text.charCodeAt(i) - 97) + (key.charCodeAt(keyIndex) - 97))%26 + 97);
				keyIndex ++;
			}
			else {
				result += text.charAt(i);
			}
		}
		return result;
	}
}

function decrypt(){
	var cipherFunction = document.getElementById("cipher").value;
	var cipherText = document.getElementById("cipherText").value.toLowerCase();
	var plainText = cipherText
	if(cipherFunction == "caeser"){
		plainText = caeserDecrypt(cipherText);
	}
	else if (cipherFunction == "otp"){
		plainText = otpDecrypt(cipherText);
	}
	document.getElementById("plainText").value = plainText;
}

function caeserDecrypt(cipherText){
	if(cipherText.length < 1) {
		alert("please enter some ciphertext (letters only)");
	}
	else {
		var shift = document.getElementById("shift").value;
	  var result = "";
		var re = /[a-z]/;
		for(i=0; i<cipherText.length; i++){
				 if(re.test(cipherText.charAt(i))){
					 result += String.fromCharCode((cipherText.charCodeAt(i) - 97 + 26 - shift)%26 + 97);
				 }
				 else {
					 result += cipherText.charAt(i);
				 }
		 }
		 return result;
	 }
}

function otpDecrypt(cipherText){
	if(cipherText.length < 1) {
		alert("please enter some ciphertext (letters only)");
	}
	else {
		var key = document.getElementById("key").value;
	  var result = "";
		var re = /[a-z]/;
		var keyIndex = 0;
		for(i=0; i < cipherText.length; i++){
				 if(re.test(cipherText.charAt(i))){
					 var code = cipherText.charCodeAt(i) - key.charCodeAt(keyIndex);
					 if (code < 0){
						 code += 26;
					 }
					 result += String.fromCharCode((code % 26) + 97);
					 keyIndex ++;
				 }
				 else {
					 result += cipherText.charAt(i);
				 }
		 }
		 return result;
	 }
}

function randomString() {
	var chars = "abcdefghijklmnopqrstuvwxyz";
	var randomstring = "";
	var text = document.getElementById("plainText").value;
	var length = text.replace(" ", "").length;
	for (var i=0; i<length; i++) {
		var rnum = Math.floor(Math.random() * 25);
		randomstring += chars.substring(rnum,rnum+1);
	}
	document.getElementById("key").value = randomstring;
}
