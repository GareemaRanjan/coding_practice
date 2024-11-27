# Question 3: Inventory Tracking System for Robot Retail Store
    # Your task is to implement an inventory tracking system for a robot retail store.
    # You are given a transaction log 'logs', where each log item corresponds to one of three transaction types: supply, sell, or upgrade.
    # Log items are provided in the following format:
    #   - ["supply", "<robot name>", "<count>", "<price>"] - the store receives <count> units of <robot name>, and each robot costs <price>.
    #   - ["sell", "<robot name>", "<count>"] - the store sells <count> units of <robot name>, at the specified price available in inventory.
    #     The store will always have enough to satisfy sell transactions.
    #   - ["upgrade", "<robot name>", "<count>", "<new price>"] - the store upgrades <count> units of <robot name> to a new version that should be sold with a higher price.
    #     It is guaranteed that there are <count> units of older version that were being sold at price <old price>.
    # The tracking system should return the revenue from all 'sell' transactions after processing the entire transaction log.
    # Specifically, return an array representing the amount of money the store received from each 'sell' transaction.

# Example:
# logs = [
#     ["supply", "robot1", "2", "100"],
#     ["supply", "robot2", "3", "60"],
#     ["sell", "robot1", "1"],
#     ["upgrade", "robot2", "1", "100"],
#     ["sell", "robot2", "1"],
#     ["sell", "robot2", "2"],
#     ["sell", "robot2", "1"]
# ]
# The output should be [100, 60, 60, 100].
# Explanation:
# 1. Supply 2 units of robot1 at price 100.
# 2. Supply 3 units of robot2 at price 60.
# 3. Sell 1 unit of robot1 at price 100. Revenue = 100.
# 4. Upgrade 1 unit of robot2 to price 100.
# 5. Sell 1 unit of robot2 at price 60. Revenue = 60.
# 6. Sell 2 units of robot2 at price 60. Revenue = 120 (split into two sells).
# 7. Sell 1 unit of robot2 at upgraded price 100. Revenue = 100.

def process_logs(logs):
    from collections import defaultdict
    res = []
    inv = defaultdict(lambda: defaultdict(int))
    for log in logs:
        if not log: continue
        op = log[0]
        if op == 'supply':
            _, r, c, p = log
            inv[r][int(p)] += int(c)
        elif op == 'upgrade':
            _, r, c, op, np = log
            c, op, np = int(c), int(op), int(np)
            avail = inv[r].get(op, 0)
            to_upgrade = min(c, avail)
            if to_upgrade:
                inv[r][op] -= to_upgrade
                if inv[r][op] == 0:
                    del inv[r][op]
                inv[r][np] += to_upgrade
        elif op == 'sell':
            _, r, c = log
            c = int(c)
            revenue = 0
            prices = sorted(inv[r])
            for p in prices:
                if c == 0: break
                qty = min(c, inv[r][p])
                revenue += qty * p
                inv[r][p] -= qty
                c -= qty
                if inv[r][p] == 0:
                    del inv[r][p]
            res.append(revenue)
    return res

# Example usage:
logs = [
    ["supply", "robot1", "2", "100"],
    ["supply", "robot2", "3", "60"],
    ["sell", "robot1", "1"],
    ["upgrade", "robot2", "1", "60", "100"],
    ["sell", "robot2", "1"],
    ["sell", "robot2", "1"],
    ["sell", "robot2", "1"]
]
print(process_logs(logs))