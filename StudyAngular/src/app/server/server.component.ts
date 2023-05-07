import { Component } from "@angular/core";

@Component({
    selector: 'app-server',
    templateUrl: './server.component.html',
    styleUrls: ['./server.component.css']
})
export class ServerComponent {
    Ids = [1, 2, 3, 4, 5];
    status: string = 'good';
    allowToClickForButton = false;
    serverName = '';

    constructor() {
        setTimeout(() => {
            this.allowToClickForButton = true;
        }, 2000);
    }

    onClick() {
        this.status = 'bad';
    }

    onUpdateServerName(event: Event) {
        this.serverName = (<HTMLInputElement>event.target).value;
    }

    // -----------------------------------------

    userName = '';

    
}




