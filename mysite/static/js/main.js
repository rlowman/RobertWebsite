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

function railFenceGroupDefault(text) {
	var groups = parseInt(document.getElementById("groups").value);
	if (!(groups > 1 && groups <= (text.length + 1)/2)) {
		groups = 3;
		document.getElementById("groupError").value = "Rail Fence count invalid; setting the amout of fences to 3."
	}
	return groups;
}

function railFenceDisplacementDefault(text, groups) {
	var displacement = parseInt(document.getElementById("displacement").value);
	if (!(displacement >= 0 && displacement <= ((2 * groups) - 2))) {
		displacement = 0;
		document.getElementById("displacementError").value = "Rail Fence count invalid; setting the amout of fences to 3."
	}
	return displacement;
}

// All valid symobls that can be included in cipher
var validSymbols = ["a", "b", "c", "d", "e", "f",
										"g", "h", "i", "j", "k", "l",
										"m", "n", "o", "p", "q", "r",
										"s", "t", "u", "v", "w", "x",
										"y", "z", " "]

function railfenceEncrypt() {
	// Retrieve necessary data from document
	var text = document.getElementById("railfencePlainText").value;
	var groups = railFenceGroupDefault(text);
	var displacement = railFenceDisplacementDefault(text, groups);
	var unreadSymbols = new Set();
	var direction = 1;
	var adjuster;
	var cipherText = "";
	var cipherFencePost	= new Array(groups);
	var cipherIncrement	= 0;

	// Set all fences to default value
	for (i = 0; i < cipherFencePost.length; i++) {
		cipherFencePost[i] = "";
	}

	// Find proper stating point
	if ((displacement - groups) < 0) {
		adjuster = displacement;
	}
	else {
		adjuster = (groups - 2 - (displacement % groups));
		direction *= -1;
	}
	cipherIncrement = displacement;
	for (i = 0; i < text.length; i++) {
		var current = text.charAt(i);
		if (validSymbols.indexOf(current) != -1) {
			cipherFencePost[adjuster] += current;
			if (adjuster > 1) {
				if (cipherIncrement % (groups - 1) == 0 && i != 0) {
					direction *= -1;
				}
			}
			else if (adjuster < 1 && direction == -1) {
				direction *= -1;
			}
			adjuster += direction;
			cipherIncrement++;
		}
		else {
			unreadSymbols.add(current);
		}
	}
	for (i = 0; i < cipherFencePost.length; i++) {
		cipherText += cipherFencePost[i];
	}
	if(unreadSymbols.size > 0) {
		var errorString = "The following symbols cannot be read: ";
		const iter = unreadSymbols.entries();
		var index = 0;
		for (let item of iter) {
			if(index == unreadSymbols.size - 1) {
				errorString += current;
			}
			else {
				errorString = errorString + current + ", ";
			}
		}
		document.getElementById("unreadSymbols").innerHTML = errorString;
	}
	document.getElementById("railfenceCipherText").value = cipherText;
}

function playfairEncrypt() {
  	var plaintext = document.getElementById("playfairPlainText").value.toLowerCase().replace(/[j]/g, "i");
    var key = document.getElementById("playfairKey").value.toLowerCase();
    // do some error checking
    if(plaintext.length < 1){
			alert("please enter some plaintext (letters and numbers only)");
			return;
		}

		// Remove unrecognized symbols
		plaintext = plaintext.replace(/[^a-z]/g, "");
		key = generateKeySquare(key.replace(/[^a-z]/g, ""));
		console.log(key);
    while(plaintext.length % 2 != 0) {
			plaintext += "x";
		}
    ciphertext = "";
    for(i=0; i<plaintext.length; i+=2) {
        a = plaintext.charAt(i);
				b = plaintext.charAt(i+1);
        if(a == b) {
					b = "x";
				}
        row1 = parseInt(key.indexOf(a) / 5);
        col1 = key.indexOf(a) % 5;
        row2 = parseInt(key.indexOf(b) / 5);
        col2 = key.indexOf(b) % 5;
        if(row1 == row2){
            if(col1 == 4) {
							c = key.charAt(row1*5);
						}
            else {
							c = key.charAt(row1*5 + col1 + 1);
						}
            if(col2 == 4) {
							d = key.charAt(row2*5);
						}
            else d = key.charAt(row2*5 + col2 + 1);
        } else if(col1 == col2){
            if(row1 == 4) {
							c = key.charAt(col1);
						}
            else {
							c = key.charAt((row1+1)*5 + col1);
						}
            if(row2 == 4) {
							d = key.charAt(col2);
						}
            else {
							d = key.charAt((row2+1)*5 + col2);
						}
        } else{
            c = key.charAt(row1*5 + col2);
            d = key.charAt(row2*5 + col1);
        }
        ciphertext += c + d;
    }
    document.getElementById("playfairCipherText").value = ciphertext;
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

// Decrypts the user-given cipher-text using a Rail Fence decipher
function railfenceDecrypt() {
	// Set up variables
	var plainText = "";
	var cipherText = document.getElementById("railfenceCipherText").value.toLowerCase();
	var groups = railFenceGroupDefault(cipherText);
	var displacement = railFenceDisplacementDefault(cipherText, groups);
	var direction = 1;
	var dir = true;
	var adjuster = displacement;
	var decipherIndex	= 0;
	var displacementIndex	= 0;
	var groupSubStringElements = new Array(groups);
	var subStringLengths	= new Array(groups);
	var arrayElementCharacterCount = new Array(groups);
	var begin	= 0;
	var finish	= 0;
	var segment = 0;
	var assignMultiple = true;

	// Initialize groupSubStringElements
	for (i = 0; i < groups; i++) {
		groupSubStringElements[i] = "";
	}
	// Initialize subStringElementLengths
	for (i = 0; i < groups; i++) {
		subStringLengths[i] = "";
	}
	// Initialize arrayElementCharacterCount
	for (i = 0; i < groups; i++) {
		arrayElementCharacterCount[i] = 0;
	}

	if ((displacement - groups) < 0) {
		segment = displacement;
	}
	else {
		segment = groups - 2 - (displacement % groups);
		assignMultiple = false;
	}

	for (i = displacement; i < (cipherText.length + displacement); i++) {
		subStringLengths[segment]++;
		if (segment > 1) {
			if (i % (groups - 1) == 0) {
				assignMultiple = !(assignMultiple);
			}
		}
		else {
			if (segment < 1 && !(assignMultiple)) {
				assignMultiple = true;
			}
		}
		if (assignMultiple) {
			segment++;
		}
		else {
			segment--;
		}
		displacementIndex++;
	}

	// Extract the substrings from cipherText
	for (i = 0; i < groups; i++) {
		finish += subStringLengths[i];
		groupSubStringElements[i] = cipherText.substring(begin, finish);
		begin	= finish;
	}

	// Set a starting point according
	// to the value of displacement
	if (displacement - groups < 0) {
		adjuster = displacement;
	}
	else {
		adjuster = (groups - 2 - (displacement % groups));
		dir = !(dir);
	}
	decipherIndex = displacement;

	// Assign the characters of groupSubStringElements to plainText
	for (i = 0; i < cipherText.length; i++) {
		if (validSymbols.indexOf(cipherText.charAt(i)) != -1) {
			plainText += groupSubStringElements[adjuster].charAt(arrayElementCharacterCount[adjuster]);
			arrayElementCharacterCount[adjuster]++;
			if (adjuster > 1) {
				if (decipherIndex % (groups - 1) == 0) {
					dir = !(dir)
				}
			}
			else {
				if (adjuster < 1 && !(dir)) {
					dir = !(dir)
				}
			}
			if (dir) {
				adjuster++;
			}
			else {
				adjuster--;
			}
			decipherIndex++;
		}
	}
	// Print unknown symbols found in cipher text
	if(unreadSymbols.length > 0) {
		var errorString = "The following symbols cannot be read: "
		for(i = 0; i < unreadSymbols.length; i++) {
			var current = unreadSymbols[i];
			// Add comma behind symbol if NOT the last symbol in set
			if(i == unreadSymbols.length - 1) {
				errorString += current;
			}
			else {
				errorString = errorString + current + ", ";
			}
		}
		document.getElementById("unreadSymbols").value = errorString;
	}
	// Print decrypted text to plain text area
	document.getElementById("railfencePlainText").value = plainText;
}

function playfairDecrypt(f) {
    ciphertext = document.getElementById("playfairCipherText").value.toLowerCase().replace(/[j]/g, "i");
    key = document.getElementById("playfairKey").value.toLowerCase();
    if(ciphertext.length < 1){
			alert("please enter some ciphertext (letters only)");
			return;
		}
    if(ciphertext.length % 2 != 0){
			alert("ciphertext length must be even.");
			return;
		}

		// Remove unknown symbols
		ciphertext = ciphertext.replace(/[^a-z]/g, "");
		key = generateKeySquare(key.replace(/[^a-z]/g, ""));
		    plaintext = "";
    for(i=0; i<ciphertext.length; i+=2){
        a = ciphertext.charAt(i);
				b = ciphertext.charAt(i+1);
        row1 = parseInt(key.indexOf(a) / 5);
        col1 = key.indexOf(a) % 5;
        row2 = parseInt(key.indexOf(b) / 5);
        col2 = key.indexOf(b) % 5;
        if(row1 == row2){
            if(col1 == 0) {
							c = key.charAt(row1*5 + 4);
						}
            else {
							c = key.charAt(row1*5 + col1 - 1);
						}
            if(col2 == 0) {
							d = key.charAt(row2*5 + 4);
						}
            else {
							d = key.charAt(row2*5 + col2 - 1);
						}
        } else if(col1 == col2){
            if(row1 == 0) {
							c = key.charAt(20 + col1);
						}
            else {
							c = key.charAt((row1-1)*5 + col1);
						}
            if(row2 == 0) {
							d = key.charAt(20 + col2);
						}
            else {
							d = key.charAt((row2-1)*5 + col2);
						}
        } else {
            c = key.charAt(row1*5 + col2);
            d = key.charAt(row2*5 + col1);
        }
        plaintext += c + d;
    }
    document.getElementById("playfairPlainText").value = plaintext.toUpperCase();
}

// Generates the keysquare needed to complete the Playfair Cipher
function generateKeySquare(key) {
	var allowed = "abcdefghiklmnopqrstuvwxyz";
	var returnValue = "";
	for (i = 0; i < key.length; i++) {
		var temp = key.charAt(i);
		if (returnValue.indexOf(temp) == -1 && returnValue.length < 25){
			returnValue += temp;
		}
	}
	for (i = 0; i < allowed.length; i++) {
		var temp = allowed.charAt(i);
		if (returnValue.indexOf(temp) == -1){
			returnValue += temp;
		}
	}
	return returnValue;
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

// Opens the selected cipher tool
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
