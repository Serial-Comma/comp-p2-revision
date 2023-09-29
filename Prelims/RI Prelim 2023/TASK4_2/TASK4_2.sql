    SELECT 
    Member.Name,
    Member.Gender,
    MAX(FitnessRecord.WorkoutDate)
    FROM Member
    LEFT JOIN FitnessRecord ON Member.MemberID = FitnessRecord.MemberID
    GROUP BY Name
    ORDER BY Gender ASC, Name ASC