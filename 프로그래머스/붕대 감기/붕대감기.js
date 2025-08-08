function solution(bandage, health, attacks) {
    let [t, x, y] = bandage
    const max_t = attacks[attacks.length - 1][0]  // 최대 시간
    const dmg = Array.from({length: max_t}, () => 0) // 시간마다 데미지 기록
    attacks.forEach(([time, damage]) => {
        dmg[time] = damage
    })
    
    let now = 0
    let combo = 0
    let now_h = health
    
    while (now < max_t) {
        now += 1
        
        if (dmg[now] != 0) {
            // 공격 받는다면, 피가 줄고 콤보도 깨짐
            now_h -= dmg[now]
            combo = 0
            if (now_h <= 0) {
                return -1
            }
        } else {
            // 체력 회복
            now_h = Math.min(now_h + x, health)
            combo += 1
            if (combo == t) {
                now_h = Math.min(now_h + y, health)
                combo = 0 
            }
        }
    }
    return now_h
}