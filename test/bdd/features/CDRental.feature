Feature: Check out CD
         and record as rented

         As the clerk, I want to check out a CD for a customer so that I can keep
         track of who has rented it.
        
         Scenario: Check out CD for a customer
         Given
             Customer has ID
             CD has ID
             CD is not currently rented
         When
             Clerk checks out CD
         Then
             CD recorded as rented
             Rental contract printed
