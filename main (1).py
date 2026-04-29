from data_entry import add_patient, save_to_csv, load_data
from analyzer import risk_analysis, disease_analysis, age_group_analysis, compare_camps

def main():
    patients = []

    while True:
        print("\n1. Add Patient")
        print("2. Save Data")
        print("3. Analyze Data")
        print("4. Compare Camps")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            patient = add_patient()
            if patient:
                patients.append(patient)
                print("Patient added successfully!")
        elif choice == "2":
            filename = input("Enter filename (e.g., camp_1.csv): ")
            save_to_csv(patients, filename)

        elif choice == "3":
            filename = input("Enter file to analyze: ")
            df = load_data(filename)
            if df is not None:
                risk_analysis(df)
                disease_analysis(df)
                age_group_analysis(df)

        elif choice == "4":
            f1 = input("Enter previous camp file: ")
            f2 = input("Enter current camp file: ")

            df1 = load_data(f1)
            df2 = load_data(f2)

            if df1 is not None and df2 is not None:
                compare_camps(df1, df2)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()