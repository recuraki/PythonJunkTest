import Rx from 'rx'

Rx.Observable.from([1, 2, 3, 4])
    .subscribe(s => console.log("from " + s));

Rx.Observable.range(1, 3)
        .map(i => i * 2)
        .subscribe(console.log.bind(console, "map"));

