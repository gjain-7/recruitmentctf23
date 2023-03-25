(async () => {
  await new Promise((res) => window.addEventListener('load', res))

  const state = {
      velocity: 0,
      angle: 0,
      time: undefined,
  }

  const element = document.querySelector('img')
  const animate = (current) => {
      if (state.time === undefined) state.time = current

      const delta = current - state.time
      state.angle = (state.angle + state.velocity * delta / 1000) % 360

      element.style.transform = `rotate(${state.angle}deg)`

      state.time = current
      requestAnimationFrame(animate)
  }
  requestAnimationFrame(animate)

  window.addEventListener('click', () => {
      state.velocity += 10;
  })

  setInterval(() => {
      state.velocity = Math.max(0, state.velocity - 1)
  }, 100)
})()

// flag part 3: EvErywHEr3}
