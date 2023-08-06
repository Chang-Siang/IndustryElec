import matplotlib.pyplot as plt

def show_history(history, title, start_from=10):
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history['mse'][start_from:], label = 'train')
    plt.plot(history['val_mse'][start_from:], color = 'red', label = 'valid')
    plt.xticks(range(start_from, len(history['loss']), 50))
    plt.ylabel('MSE')
    plt.xlabel('Epoch')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history['mae'][start_from:], label = 'train')
    plt.plot(history['val_mae'][start_from:], color = 'red', label = 'valid')
    plt.xticks(range(start_from, len(history['loss']), 50))
    plt.ylabel('MAE')
    plt.xlabel('Epoch')
    plt.legend()
    
    plt.suptitle(F"Training History: {title}")
    plt.savefig(F"logs/{title.lower().replace(' ', '_')}.jpg", bbox_inches='tight', pad_inches=0.05)
    plt.show()
    
def show_error(real, pred, index, title):
    plt.figure(figsize=(12, 4))
    plt.plot(index, real, color='red', label='Real')
    plt.plot(index, pred, color='blue', label='Pred')
    plt.title(F"Power Consumption Prediction: {title}")
    plt.ylabel('Power Consumption (MkWh)')
    plt.legend()
    plt.savefig(F"results/{title.lower().replace(' ', '_')}.jpg", bbox_inches='tight', pad_inches=0.05)
    plt.show()