function solution(board, moves) {
    let stack = [0];
    let topi = 0;
    let cnt = 0;
    let N = board.length;
    for(let i = 0; i < moves.length; i++){
        let col = moves[i] - 1;
        // console.log(col,'열',board)
        for(let row = 0; row < N; row++){
            if(board[row][col] !== 0){
                // console.log(row,'행',board[row][col],stack[topi])
                
                if(board[row][col] === stack[topi]){
                    // console.log(board[row][col],'터짐')
                    stack.pop()
                    cnt += 2;
                    topi--;
                }
                else{
                    stack.push(board[row][col]);
                    topi++;
                }
                board[row][col] = 0;
                break;
            }
        }
        // console.log('after', stack)
    }
    return cnt;
}