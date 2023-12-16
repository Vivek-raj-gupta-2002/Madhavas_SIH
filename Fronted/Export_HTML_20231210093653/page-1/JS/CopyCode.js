async function copyText() {
    // Get the text from the <p> tag
    console.log('hi');
    var text = document.getElementById("textToCopy").innerText;

    try {
      // Use the Clipboard API to write text to the clipboard
      await navigator.clipboard.writeText(text);
    } catch (err) {
      console.error('Unable to copy text', err);
    }



}