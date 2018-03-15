// Encrypts the user-given plain-text using a Caeser cipher
function caeserEncrypt(){
	var text = document.getElementById("caeserPlainText").value.toLowerCase();
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
		document.getElementById("caeserCipherText").value = result;
	}
}

// Encrypts the user-given plain-text using a One Time Pad cipher
function otpEncrypt(){
	var text = document.getElementById("otpPlainText").value.toLowerCase();
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
		document.getElementById("otpCipherText").value = result;
	}
}

// Decrypts the user-given cipher-text using a caeser decipher
function caeserDecrypt(){
	var cipherText = document.getElementById("caeserCipherText").value.toLowerCase();
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
		 document.getElementById("caeserPlainText").value = result;
	 }
}

// Decrypts the user-given cipher-text using a One Time Pad decipher
function otpDecrypt(){
	var cipherText = document.getElementById("otpCipherText").value.toLowerCase();
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
		 document.getElementById("otpPlainText").value = result;
	 }
}

/*
Creates a pseudo-random string for One Time Pad encryption
NOTICE: This does not create a truely-random pad that is required for a true
One Time Pad cipher. Also, this key should be deleted after decryption to ensure
full secrecy.
*/
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

function openCipher(evt, cipher) {
	// Declare all variables
	var i, tabcontent, tablinks;

	// Get all elements with class="tabcontent" and hide them
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
			tabcontent[i].style.display = "none";
	}

	// Get all elements with class="tablinks" and remove the class "active"
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
			tablinks[i].className = tablinks[i].className.replace(" active", "");
	}

	// Show the current tab, and add an "active" class to the button that opened the tab
	document.getElementById(cipher).style.display = "block";
	evt.currentTarget.className += " active";
}
