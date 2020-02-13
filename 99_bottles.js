function bottleSong() {
  let bottleCount = 99
  do {
    if (bottleCount > 1) {
      console.log(`${bottleCount} bottles of beer on the wall, ${bottleCount} bottles of beer.`)
      bottleCount -= 1
      console.log(`Take one down and pass it around,  ${bottleCount} bottles of beer on the wall.`)
    } else if (bottleCount === 1) {
      console.log(`${bottleCount} bottle of beer on the wall, ${bottleCount} bottle of beer.`)
      bottleCount -= 1
      console.log("Take one down and pass it around, no more bottles of beer on the wall.")
      console.log("No more bottles of beer on the wall, no more bottles of beer.")
    }
    // } else if(bottleCount === 0){
    //   console.log(`Go to the store and buy more, `)
    // }

  } while (bottleCount >= 0)
};

bottleSong();
