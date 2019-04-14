/* PURPOSE: Create a Java program to read a file of floating point
 * numbers and compute the maximum, minimum, arithmetic average(mean),
 * and standard deviation from the data. 
 * Name: Kaivan Taylor
 * CSC 201 - Computer Science I
 * Professor Seaman
 */

import java.io.*;
import java.util.Scanner;

public class DataFiles {
	public static void main(String[] args) {
		// Local Variables of type double for consistency
		double line_double;
		double count = 0; // Consistent variables

		double sum_square_double = 0; // Variables for Standard Deviation
		double line_double_squared;
		double m_squared;
		double sum_x_square_count;
		double s;
		double s_squared;

		double sum_double = 0; // Variables for Mean
		double average;

		double maximum_double = 0; // Variable for Maximum
		double minimum_double = 0; // Variable for Minimum

		Scanner inputStream = null;

		// try-catch for IO errors.
		try {
			inputStream = new Scanner(new File("RawData.txt"));
		} catch (FileNotFoundException e) {
			System.out.println("Error opening file; program aborted.");
		}

		// Loop to read each number from file.
		while (inputStream.hasNextDouble()) {
			count = count + 1; // Adds 1 count for every double.
			line_double = inputStream.nextDouble(); // Read second double.
			line_double_squared = line_double * line_double; // Calculate double squared.
			sum_square_double = sum_square_double + line_double_squared; // Calculate sum of doubles squared.

			sum_double = sum_double + line_double; // Calculate sum of doubles.

			// First instance of reading in while loop. x is min. and max.
			if (maximum_double == 0 && minimum_double == 0) {
				maximum_double = line_double;
				minimum_double = line_double;
				// If x is greater than max., make it the new max.
			} else if (line_double > maximum_double) {
				maximum_double = line_double;
				// If x is less than min., make it the new min.
			} else if (line_double < minimum_double) {
				minimum_double = line_double;
			}
			else{
				; // Pass or do nothing.
			}
		}

		System.out.println("Count:");
		System.out.println(count);

		average = sum_double / count; // Sum of all x's divided by the number x's.
		System.out.println("The average is:");
		System.out.println(Math.floor(average * 100) / 100);

		sum_x_square_count = sum_square_double / count; // Sum of x's squared divided by count.
		m_squared = average * average; // Average squared.
		s_squared = sum_x_square_count - m_squared; // Difference of (sum x^2 / count)- average ^2.
		s = Math.sqrt(s_squared); // Square root of s.
		System.out.println("Standard Deviation:");
		System.out.println(Math.floor(s * 100) / 100);
		// System.out.println(m_squared); // System.out.println(sum_square_double)

		System.out.println("Maximum:");
		System.out.println(maximum_double);
		System.out.println("Minimum:");
		System.out.println(minimum_double);

		inputStream.close(); // Close reading the file.
	}
}
