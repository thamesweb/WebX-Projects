let display = document.getElementById('display');
let buttons = Array.from(document.getElementsByClassName('button'));

buttons.map(button => {
    button.addEventListener('click', (event) => {
        switch (event.target.innerText) {
            case 'C':
                display.innerText = '';
                break;
            case '=':
                try {
                    display.innerText = eval(display.innerText);
                }
                catch {
                    display.innerText = 'Invalid expression';
                }
                break;
            case '←':
                display.innerText = display.innerText.slice(0, -1);
                break;
            case 'sqrt':
                let x = display.innerText;
                display.innerText = Math.sqrt(x);
                break;
            case 'sin':
                let y= display.innerText;
                display.innerText = Math.sin(y);
                break;
            case 'cos':
                let z= display.innerText;
                display.innerText = Math.cos(z);
                break;
            case 'tan':
                let t = display.innerText;
                display.innerText = Math.tan(t);
                break;
            default:
                display.innerText += event.target.innerText;
                
       }
    })
})