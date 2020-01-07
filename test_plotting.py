import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')                                                                                                                                                                                
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

fig2 = plt.figure(figsize=(8,4))
fig2Grid = plt.GridSpec(8, 12, figure=fig2, hspace=0.1, wspace=0.1)
ax = []

numBins = list(range(-150, 151, 2))

mu = [-95, -50, 0, 45, 100]
sigma = [10, 15, 5, 4, 25]
ax.append(fig2.add_subplot(fig2Grid[:, :], xlim=[-150, 150], ylim=[0, 0.20], xticklabels=[], yticklabels=[]))
# ax.append(fig2.add_subplot(fig2Grid[4:, :], xlim=[-150, 150], ylim=[1e-7, 0.15], xticklabels=[], yticklabels=[], yscale="log"))


for i in range(len(mu)):
        data = mu[i] + sigma[i] * np.random.randn(5000)
        hist, binEdges = np.histogram(data, bins=numBins, density=1)
        x0 = np.linspace(min(data)-50, max(data)+50, 1000)
        y0 = (1 / (np.sqrt(2 * np.pi) * sigma[i])) * np.exp(-0.5 * (1 / sigma[i] * ( x0 - mu[i] ))**2)
        ax[0].bar(binEdges[:-1], hist, width=2.0, bottom=0, edgecolor='black', linewidth=0.5, fc='none')
        ax[0].plot(x0, y0, color=colors[i], linewidth=0.75)
        ax[0].fill_between(x0[x0>=mu[i]], 0, y0[x0>=mu[i]], color=colors[i], alpha=0.80)
        ax[0].fill_between(x0[(x0 >= mu[i] - 4.3702*sigma[i]) & (x0 <= mu[i])], 0, y0[(x0 >= mu[i] - 4.3702*sigma[i]) & (x0 <= mu[i])], color=colors[i], alpha=0.40)
        ax[0].fill_between(x0[x0 <= mu[i] - 4.3702*sigma[i]], 0, y0[x0 <= mu[i] - 4.3702*sigma[i]], color=colors[i], alpha=0.10)
        if i == 1:
                ax.append(fig2.add_subplot(fig2Grid[:2, :3], xlim=[min(x0)-5, max(x0)+5], ylim=[6e-9, 0.20], xticklabels=[], yticklabels=[], yscale="log"))
                ax[1].bar(binEdges[:-1], hist, width=2.0, bottom=0, edgecolor='black', linewidth=0.5, fc='none')
                ax[1].plot(x0, y0, color=colors[i], linewidth=0.75)
                ax[1].fill_between(x0[x0>=mu[i]], 0, y0[x0>=mu[i]], color=colors[i], alpha=0.80)
                ax[1].fill_between(x0[(x0 >= mu[i] - 4.3702*sigma[i]) & (x0 <= mu[i])], 0, y0[(x0 >= mu[i] - 4.3702*sigma[i]) & (x0 <= mu[i])], color=colors[i], alpha=0.40)
                ax[1].fill_between(x0[x0 <= mu[i] - 4.3702*sigma[i]], 0, y0[x0 <= mu[i] - 4.3702*sigma[i]], color=colors[i], alpha=0.10)

        # ax[1].bar(binEdges[:-1], hist, width=2.0, bottom=0, edgecolor='black', linewidth=0.5, fc='none')
        # ax[1].plot(x0, y0, color=colors[i], linewidth=0.75)
        # ax[1].fill_between(x0[x0>=mu[i]], 0, y0[x0>=mu[i]], color=colors[i], alpha=0.80)
        # ax[1].fill_between(x0[(x0 >= mu[i] - 4.3702*sigma[i]) & (x0 <= mu[i])], 0, y0[(x0 >= mu[i] - 4.3702*sigma[i]) & (x0 <= mu[i])], color=colors[i], alpha=0.40)
        # ax[1].fill_between(x0[x0 <= mu[i] - 4.3702*sigma[i]], 0, y0[x0 <= mu[i] - 4.3702*sigma[i]], color=colors[i], alpha=0.10)

plt.show()