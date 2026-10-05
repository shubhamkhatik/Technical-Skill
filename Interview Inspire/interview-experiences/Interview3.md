# React js with typescript machine coding

## Problem Statement:

You're given an API endpoint with a list of users. Build a page that:
Displays a list of users with some basic details
Has a search input to filter users by name
Includes a dropdown filter based on user category (e.g., gender, age group, etc.)
API Endpoint:
[https://dummyjson.com/users](https://dummyjson.com/users)

Fetch and display user data
Implement a clean UI using reusable components
Add working filters (search + dropdown)
Show a sense of structure, state management, and code modularity

## Solution:

What Are We Building?
A React (with TypeScript) page that:

Fetches user data from an API (https://dummyjson.com/users)

Displays users with basic information

Provides a search input to filter users by name

Provides a dropdown filter (e.g., by gender)

Utilizes clean, reusable component structure

## Demonstrates clear state management and modularity

### a. Fetching & Managing User Data

Store the complete user dataset in a dedicated state (users).

Maintain separate states for UI filters and the filtered result (filteredUsers).

Use a custom hook for API logic to keep components focused on rendering.

// hooks/useFetchUsers.ts

```typescript
import { useState, useEffect } from "react";

type User = {
  id: number;
  firstName: string;
  lastName: string;
  gender: string;
  // ...add any additional fields you need
};

export function useFetchUsers() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("https://dummyjson.com/users")
      .then((res) => res.json())
      .then((d) => setUsers(d.users))
      .catch(() => setError("Failed to fetch users"))
      .finally(() => setLoading(false));
  }, []);

  return { users, loading, error };
}
```

### b. Search Input for Filtering by Name

State: searchText

Handler: Updates searchText as the user types.

Logic: Apply case-insensitive filter using .includes()

// components/SearchInput.tsx

```tsx
type Props = { value: string; onChange: (v: string) => void };
const SearchInput: React.FC<Props> = ({ value, onChange }) => (
  <input
    type="text"
    placeholder="Search by name..."
    value={value}
    onChange={(e) => onChange(e.target.value)}
  />
);
```

### c. Dropdown Filter (e.g., by Gender)

State: selectedGender

Derive dropdown options from the user dataset to keep it generic and reusable.

Handler: Updates selectedGender when changed.

// components/DropdownFilter.tsx

```tsx
type Option = { label: string; value: string };
type Props = {
  options: Option[];
  value: string;
  onChange: (v: string) => void;
};
const DropdownFilter: React.FC<Props> = ({ options, value, onChange }) => (
  <select value={value} onChange={(e) => onChange(e.target.value)}>
    <option value="">All</option>
    {options.map((o) => (
      <option key={o.value} value={o.value}>
        {o.label}
      </option>
    ))}
  </select>
);
```

### d. Filtering Logic and State Management

Filter users whenever searchText or selectedGender changes, using useEffect.

Keep both the full list and current filtered users in state.

```typescript
const [searchText, setSearchText] = useState<string>("");
const [selectedGender, setSelectedGender] = useState<string>("");
const [filteredUsers, setFilteredUsers] = useState<User[]>(users);

useEffect(() => {
  let result = users;
  if (searchText) {
    result = result.filter((user) =>
      `${user.firstName} ${user.lastName}`
        .toLowerCase()
        .includes(searchText.toLowerCase())
    );
  }
  if (selectedGender) {
    result = result.filter((user) => user.gender === selectedGender);
  }
  setFilteredUsers(result);
}, [searchText, selectedGender, users]);
```

### e. Displaying User List & Structuring Components

Use a reusable UserCard for each user.

Create a parent UserList to render all cards.

// components/UserCard.tsx

```tsx
type UserProps = { user: User };
const UserCard: React.FC<UserProps> = ({ user }) => (
  <div>
    <strong>
      {user.firstName} {user.lastName}
    </strong>{" "}
    - {user.gender}
  </div>
);
```

### f. Bringing It All Together in the Page

// pages/UsersPage.tsx

```tsx
import { useFetchUsers } from "./hooks/useFetchUsers";
import SearchInput from "./components/SearchInput";
import DropdownFilter from "./components/DropdownFilter";
import UserCard from "./components/UserCard";

const UsersPage: React.FC = () => {
  const { users, loading, error } = useFetchUsers();
  const [searchText, setSearchText] = useState("");
  const [selectedGender, setSelectedGender] = useState("");
  const [filteredUsers, setFilteredUsers] = useState<User[]>(users);

  useEffect(() => {
    let result = users;
    if (searchText) {
      result = result.filter((u) =>
        `${u.firstName} ${u.lastName}`
          .toLowerCase()
          .includes(searchText.toLowerCase())
      );
    }
    if (selectedGender) {
      result = result.filter((u) => u.gender === selectedGender);
    }
    setFilteredUsers(result);
  }, [searchText, selectedGender, users]);

  const genderOptions = [
    ...Array.from(new Set(users.map((u) => u.gender))),
  ].map((gender) => ({ label: gender, value: gender }));

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <>
      <SearchInput value={searchText} onChange={setSearchText} />
      <DropdownFilter
        options={genderOptions}
        value={selectedGender}
        onChange={setSelectedGender}
      />
      {filteredUsers.map((u) => (
        <UserCard key={u.id} user={u} />
      ))}
    </>
  );
};
```

Note: The `genderOptions` array is derived from the dataset to avoid hardcoding and duplicates, keeping the UI dynamic and consistent with the data.

## Summary Table: Key Concepts

| Concept                       | What            | Why              | How                                    | Where/When                           |
| :---------------------------- | :-------------- | :--------------- | :------------------------------------- | :----------------------------------- |
| Custom Hook (`useFetchUsers`) | Fetch users     | Abstract logic   | `useEffect` + state                    | Any data fetch scenario              |
| Search Input                  | Filter by name  | Enhance UX       | Input component                        | Any searchable list feature          |
| Dropdown Filter               | Category filter | Easy grouping    | Select component                       | Filtering by gender/other category   |
| Filter Logic                  | Combine filters | Accurate results | `useEffect` + `Array.prototype.filter` | Whenever search/filter state changes |
| Reusable Components           | Modular UI      | Scalable code    | Separate files                         | Whenever the same UI pattern repeats |
