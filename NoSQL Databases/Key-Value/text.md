# Redis

## Redis Cloud
- Redis Database
- Data persistance
- JSON support
- Search
- Redis OM (object mapping)

## Redis Data Types
1. Strings
	name --> 'mario'
	age  --> '30'
2. Sets
	names --> {'mario', 'taya', 'brett'}
3. Hashes
	book --> {
		   title: 'The inception'
		   genre: 'Science fiction'
		  }
4. Lists
	names --> {'taya', 'brett', 'taya', 'cooper'}
5. Sorted sets
	names --> {
		    'taya': 1,
		    'brett': 2,
		    'cooper': 3
		  }
## STRING DATA TYPE

### Common Commands
1. SET key value
2. GET key
3. DEL key
4. MSET key1 value1 key2 value2 key3 value3...
5. MGET key1 key2 key3...
6. GETRANGE key startIndex endIndex
7. SETRANGE key start offset
8. INCR key
9. DECR key
10. INCRBY key increment
11. DECRBY key decrement

- [Redis docs](https://redis.io/docs/latest/operate/oss_and_stack/install/)

### Command Options
- Flags
- For example
#### SET command
1. EX seconds - data expire time
2. PX
3. EXAT
4. PXAT
5. NX
6. XX

## SET DATA TYPE
- Members must be unique
- Creating set
	- SADD key values
- Removing a member from the set
	- SREM key value
- Combining two or more sets together(N/B: only return combine sets but does not combine them in the db)
	- SUNION key1 key2
- Checking if the particular member exist in the set
	- SISMEMBER key member
- etc

## LIST DATA TYPE

- Members in the list do not need to be unique
- N/B: List in redis is almost similar as singly linked list
- Adding members to the list
	1. RPUSH key values (Right push)
	2. LPUSH key values (Left push)
- Popping members from the list
	1. LPOP key index
	2. RPOP key index
- LLEN key
- LRANGE key start end
- Getting member from specific index
	- LINDEX key index
- Getting the index of the member
	- LPOS key member

## HASH DATA TYPE

- N/B: It is similar to objects
- Naming conventions
	- If the multiple entries for the specific key, we use colon followed be id
	- For example: user:1, user:2 etc
- Adding a hash
	- HSET key field1 value1...
- Getting a field value from the hash
	- HGET key field
- To get all the fields with their values
	- HGETALL key
- To check if a property exists in the hash
	- HEXISTS key field
- To get all the fields in the hash
	- HKEYS key
- Deleting a field from the hash
	- HDEL key field1...
- Deleting the entire hash
	- DEL key
- HVALS key
