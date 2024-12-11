# /**
# 	 * 
# 	 * @param n the number of people standing in the circle
# 	 * @return the safe position who will survive the execution 
# 	 *   f(N) = 2L + 1 where N =2^M + L and 0 <= L < 2^M
# 	 */
# 	public int getSafePosition(int n) {
# 		// find value of L for the equation
# 		int valueOfL = n - Integer.highestOneBit(n);
# 		int safePosition = 2 * valueOfL  + 1;
		
# 		return safePosition;
# 	}

# valueOfL = n- Integer.highestOneBit(316454)
# safePosition = 2 * valueOfL + 1
import math

seats = 3014603

index = int(math.log(seats, 2))
valueOfL = seats - (1<<index)
safePosition = 2 * valueOfL + 1

print safePosition