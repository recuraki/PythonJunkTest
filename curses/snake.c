#include <curses.h>
#include <unistd.h>
#include <time.h>
#define STAGESIZE  40
#define TAIL_NUM ((STAGESIZE-2)*(STAGESIZE-2))
int tail_x[TAIL_NUM];
int tail_y[TAIL_NUM];
int tail_top, tail_end;
int main(void)
{
    int i,d,ch,v;
    int px,py,vx,vy;
    srand(time(NULL));
    if(!initscr())return 1;
    noecho();nonl();cbreak();
    wtimeout(stdscr, 0);
    keypad(stdscr, TRUE);
    leaveok(stdscr, TRUE);
RETRY:
    curs_set(0);
    clear();
    for(py=0;py<STAGESIZE;++py)
        for(px=0;px<STAGESIZE;++px)
            mvaddch(py,px,'.');
    for(i=0;i<STAGESIZE;++i){
        mvaddch(i,0,'#');
        mvaddch(0,i,'#');
        mvaddch(i,STAGESIZE-1,'#');
        mvaddch(STAGESIZE-1,i,'#');
    }
    tail_top=tail_end=0;
    py=1; px=1;
    vx=1; vy=0;
    for(d=1;;++d){
        usleep(100000);
        ch=getch();
        if(v=-(ch==KEY_LEFT)+(ch==KEY_RIGHT))vx=v,vy=0;
        if(v=-(ch==KEY_UP)+(ch==KEY_DOWN))vy=v,vx=0;
        tail_x[tail_top]=px;
        tail_y[tail_top]=py;
        mvaddch(py,px,'o');
        mvaddch(tail_y[tail_end],tail_x[tail_end],'.');
        px+=vx;py+=vy;
        move(py,px);
        ch=inch();
        addch('&');
        if(ch!='*'&&ch!='.')break;
        if(d%10==0){
            mvaddch(rand()%(STAGESIZE-2)+1,rand()%(STAGESIZE-2)+1,'*');
        }
        ++tail_top;tail_top%=TAIL_NUM;
        if(ch!='*'){
            ++tail_end;tail_end%=TAIL_NUM;
        }
        refresh();
    }
    curs_set(1);
    mvaddstr(STAGESIZE,0,"retry or quit [r/q] ?");
    refresh();
    do {
        ch=getch();
        if(ch == 'r') {
            goto RETRY;
        }
    } while(ch != 'q');
    endwin();
    return 0;
}
